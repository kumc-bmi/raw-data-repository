from abc import ABC, abstractmethod
from enum import Enum
from typing import List

from rdr_service import clock
from rdr_service.cloud_utils.gcp_cloud_tasks import GCPCloudTask
from rdr_service.config import GAE_PROJECT
from rdr_service.genomic_enums import GenomicJob, GenomicLongReadPlatform, GenomicIncidentCode


class GenomicBaseSubWorkflow(ABC):

    def __init__(self, dao, job_id, job_run_id, **kwargs):
        self.dao = dao()
        self.job_id = job_id
        self.job_run_id = job_run_id
        self.row_data = []
        self.current_manifest_file_name = kwargs.get('manifest_file_name', None)

        self.genome_type = None
        self.site_id = None
        self.increment_set_number = None

    def get_sub_workflow_method(self):
        sub_workflow_map = {
            GenomicJob.PR_PR_WORKFLOW: self.run_request_ingestion,
            GenomicJob.PR_P1_WORKFLOW: self.run_sample_ingestion,
            GenomicJob.RNA_RR_WORKFLOW: self.run_request_ingestion,
            GenomicJob.RNA_R1_WORKFLOW: self.run_sample_ingestion,
            GenomicJob.LR_LR_WORKFLOW: self.run_request_ingestion,
            GenomicJob.LR_L1_WORKFLOW: self.run_sample_ingestion
        }
        return sub_workflow_map.get(self.job_id)

    @classmethod
    def create_genomic_sub_workflow(cls, *, dao, job_id, job_run_id, **kwargs):
        return cls(dao, job_id, job_run_id, **kwargs)

    @classmethod
    def execute_cloud_task(cls, payload: dict, endpoint: str, task_queue='genomics'):
        if GAE_PROJECT != 'localhost':
            cloud_task = GCPCloudTask()
            cloud_task.execute(
                endpoint=endpoint,
                payload=payload,
                queue=task_queue
            )

    def set_model_string_attributes(self) -> List[str]:
        return [str(obj).split('.')[-1] for obj in self.dao.model_type.__table__.columns]

    def extract_site_id(self) -> str:
        current_site_id = None
        first_row: dict = self.row_data[0]
        try:
            current_site_key = [obj for obj in first_row if '_site_id' in obj]
            if current_site_key:
                current_site_id = first_row.get(current_site_key[0])
        except KeyError:
            ...
        return current_site_id

    @abstractmethod
    def set_default_base_attributes(self) -> dict: return {}

    def build_defaulted_base_attributes(self, model_string_attributes: List[str]) -> dict:
        base_default_attributes_map = {
            '_site_id': self.site_id,
            '_set': self.increment_set_number
        }
        defaulted_base_obj = self.set_default_base_attributes()
        current_base_attributes = {
            **defaulted_base_obj,
            **{'id': None, 'genomic_set_member_id': None}
        }

        filtered_model_attributes = [str(obj).split('.')[-1] for obj in model_string_attributes
                                     if str(obj).split('.')[-1] not in current_base_attributes]

        for attribute_string in filtered_model_attributes:
            for obj in base_default_attributes_map:
                if obj in attribute_string:
                    defaulted_base_obj[attribute_string] = base_default_attributes_map.get(obj)

        return defaulted_base_obj

    def get_incremented_set_number(self) -> int:
        current_set: List[int] = self.dao.get_max_set()
        return 1 if current_set[0] is None else current_set[0]+1

    @classmethod
    def get_base_member_attributes(cls, new_member) -> dict:
        return {
            'genomic_set_member_id': new_member.genomic_set_member_id,
            'biobank_id': new_member.biobank_id,
            'collection_tube_id': new_member.collection_tube_id
        }

    def set_instance_attributes_from_data(self) -> None:
        self.genome_type = self.row_data[0].get('genome_type', None)
        self.site_id = self.extract_site_id()
        self.increment_set_number = self.get_incremented_set_number()

    def run_workflow(self, *, row_data) -> None:
        self.row_data = row_data
        self.set_instance_attributes_from_data()
        executed_sub_workflow = self.get_sub_workflow_method()
        if not executed_sub_workflow:
            return
        executed_sub_workflow()

    def handle_request_differences(self, *, request_biobank_ids: List[str], returned_biobank_ids: List[str]) -> None:
        missing_in_returned = list(set(request_biobank_ids) - set(returned_biobank_ids))
        if not missing_in_returned:
            return

        message = (f'{self.job_id.name}: Biobank IDs [{",".join(missing_in_returned)}] failed request manifest '
                   f'validation: {self.current_manifest_file_name}')
        self.execute_cloud_task(
            payload={
                'slack': True,
                'source_job_run_id': self.job_run_id,
                'code': GenomicIncidentCode.REQUEST_MANIFEST_VALIDATION_FAIL.name,
                'message': message,
                'manifest_file_name': self.current_manifest_file_name,
            },
            endpoint='genomic_incident'
        )

    def run_request_ingestion(self) -> None:
        model_string_attributes: List[str] = self.set_model_string_attributes()
        request_biobank_ids = [row.get('biobank_id')[1:] for row in self.row_data]

        new_pipeline_members = self.dao.get_new_pipeline_members(
            biobank_ids=request_biobank_ids,
        )

        returned_biobank_ids = [obj.biobank_id for obj in new_pipeline_members]
        pipeline_objs = []
        default_attributes: dict = self.build_defaulted_base_attributes(model_string_attributes)

        for member in new_pipeline_members:
            member_attributes = self.get_base_member_attributes(new_member=member)
            pipeline_objs.append({
                **member_attributes,
                **default_attributes,
            })

        self.dao.insert_bulk(pipeline_objs)

        self.handle_request_differences(
            request_biobank_ids=request_biobank_ids,
            returned_biobank_ids=returned_biobank_ids
        )

    def get_members_for_sample_update(self):
        return self.dao.get_pipeline_members_missing_sample_id(
            biobank_ids=[row.get('biobank_id')[1:] for row in self.row_data if row.get('sample_id')],
            collection_tube_ids=[row.get('collection_tubeid') for row in self.row_data if row.get('sample_id')]
        )

    def run_sample_ingestion(self) -> None:
        updated_pipeline_members = self.get_members_for_sample_update()
        update_objs = []
        for member in updated_pipeline_members:
            matching_row = list(filter(lambda x: x.get('biobank_id')[1:] == member.biobank_id, self.row_data))
            update_objs.append({
                'id': member.id,
                'modified': clock.CLOCK.now(),
                'sample_id': matching_row[0].get('sample_id')
            })

        self.dao.bulk_update(update_objs)


class GenomicSubWorkflow(GenomicBaseSubWorkflow):

    def set_default_base_attributes(self) -> dict:
        return {
            'created': clock.CLOCK.now(),
            'modified': clock.CLOCK.now(),
            'created_job_run_id': self.job_run_id,
            'genome_type': self.genome_type,
            'sample_id': None,
            'ignore_flag': 0
        }


class GenomicSubProWorkflow(GenomicSubWorkflow):

    def get_p_site_id(self):
        try:
            return self.current_manifest_file_name.lower().split('_')[0]
        except KeyError:
            return None

    def get_members_for_sample_update(self):
        return self.dao.get_pipeline_members_missing_sample_id(
            biobank_ids=[row.get('biobank_id')[1:] for row in self.row_data if row.get('sample_id')],
            collection_tube_ids=[row.get('collection_tubeid') for row in self.row_data if row.get('sample_id')],
            p_site_id=self.get_p_site_id()
        )


class GenomicSubRNAWorkflow(GenomicSubWorkflow):

    def get_r_site_id(self):
        try:
            return self.current_manifest_file_name.lower().split('_')[0]
        except KeyError:
            return None

    def get_members_for_sample_update(self):
        return self.dao.get_pipeline_members_missing_sample_id(
            biobank_ids=[row.get('biobank_id')[1:] for row in self.row_data if row.get('sample_id')],
            collection_tube_ids=[row.get('collection_tubeid') for row in self.row_data if row.get('sample_id')],
            r_site_id=self.get_r_site_id()
        )


class GenomicSubLongReadWorkflow(GenomicBaseSubWorkflow):

    def get_platform_value(self, attribute_name: str = 'long_read_platform') -> Enum:
        row_long_read_platform = self.row_data[0].get(attribute_name)
        return GenomicLongReadPlatform.lookup_by_name(row_long_read_platform.upper())

    def get_lr_site_id(self):
        return self.row_data[0].get('lr_site_id').lower()

    def get_members_for_sample_update(self):
        return self.dao.get_pipeline_members_missing_sample_id(
            biobank_ids=[row.get('biobank_id')[1:] for row in self.row_data if row.get('sample_id')],
            collection_tube_ids=[row.get('collection_tubeid') for row in self.row_data if row.get('sample_id')],
            long_read_platform=self.get_platform_value(),
            lr_site_id=self.get_lr_site_id()
        )

    def set_default_base_attributes(self) -> dict:
        return {
            'created': clock.CLOCK.now(),
            'modified': clock.CLOCK.now(),
            'created_job_run_id': self.job_run_id,
            'genome_type': self.genome_type,
            'sample_id': None,
            'ignore_flag': 0,
            'long_read_platform': self.get_platform_value()
        }
