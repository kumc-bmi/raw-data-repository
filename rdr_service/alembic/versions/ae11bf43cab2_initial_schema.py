"""Initial schema

Revision ID: ae11bf43cab2
Revises:
Create Date: 2017-04-04 11:13:10.154107

"""
import model.utils
import sqlalchemy as sa
from alembic import op

from rdr_service.model.code import CodeType
from rdr_service.participant_enums import (
    EnrollmentStatus,
    PhysicalMeasurementsStatus,
    QuestionnaireStatus,
    Race,
    SampleStatus,
    SuspensionStatus,
    WithdrawalStatus,
)

# revision identifiers, used by Alembic.
revision = "ae11bf43cab2"
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()


def upgrade_metrics():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_metrics():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def upgrade_rdr():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "code_book",
        sa.Column("code_book_id", sa.Integer(), nullable=False),
        sa.Column("created", model.utils.UTCDateTime(), nullable=False),
        sa.Column("latest", sa.Boolean(), nullable=False),
        sa.Column("name", sa.String(length=80), nullable=False),
        sa.Column("system", sa.String(length=255), nullable=False),
        sa.Column("version", sa.String(length=80), nullable=False),
        sa.PrimaryKeyConstraint("code_book_id"),
        sa.UniqueConstraint("system", "version"),
    )
    hpo_table = op.create_table(
        "hpo",
        sa.Column("hpo_id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("name", sa.String(length=20), nullable=True),
        sa.PrimaryKeyConstraint("hpo_id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "log_position",
        sa.Column("log_position_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("log_position_id"),
    )
    op.create_table(
        "metrics_version",
        sa.Column("metrics_version_id", sa.Integer(), nullable=False),
        sa.Column("in_progress", sa.Boolean(), nullable=False),
        sa.Column("complete", sa.Boolean(), nullable=False),
        sa.Column("date", model.utils.UTCDateTime(), nullable=False),
        sa.Column("data_version", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("metrics_version_id"),
    )
    op.create_table(
        "questionnaire",
        sa.Column("questionnaire_id", sa.Integer(), nullable=False),
        sa.Column("version", sa.Integer(), nullable=False),
        sa.Column("created", model.utils.UTCDateTime(), nullable=False),
        sa.Column("last_modified", model.utils.UTCDateTime(), nullable=False),
        sa.Column("resource", sa.BLOB(), nullable=False),
        sa.PrimaryKeyConstraint("questionnaire_id"),
    )
    op.create_table(
        "questionnaire_history",
        sa.Column("questionnaire_id", sa.Integer(), nullable=False),
        sa.Column("created", model.utils.UTCDateTime(), nullable=False),
        sa.Column("last_modified", model.utils.UTCDateTime(), nullable=False),
        sa.Column("resource", sa.BLOB(), nullable=False),
        sa.Column("version", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("questionnaire_id", "version"),
    )
    op.create_table(
        "code",
        sa.Column("code_id", sa.Integer(), nullable=False),
        sa.Column("system", sa.String(length=255), nullable=False),
        sa.Column("value", sa.String(length=80), nullable=False),
        sa.Column("display", sa.UnicodeText(), nullable=True),
        sa.Column("topic", sa.UnicodeText(), nullable=True),
        sa.Column("code_type", model.utils.Enum(CodeType), nullable=False),
        sa.Column("mapped", sa.Boolean(), nullable=False),
        sa.Column("created", model.utils.UTCDateTime(), nullable=False),
        sa.Column("code_book_id", sa.Integer(), nullable=True),
        sa.Column("parent_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["code_book_id"], ["code_book.code_book_id"]),
        sa.ForeignKeyConstraint(["parent_id"], ["code.code_id"]),
        sa.PrimaryKeyConstraint("code_id"),
        sa.UniqueConstraint("system", "value"),
    )
    op.create_table(
        "metrics_bucket",
        sa.Column("metrics_version_id", sa.Integer(), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("hpo_id", sa.String(length=20), nullable=False),
        sa.Column("metrics", sa.BLOB(), nullable=False),
        sa.ForeignKeyConstraint(["metrics_version_id"], ["metrics_version.metrics_version_id"]),
        sa.PrimaryKeyConstraint("metrics_version_id", "date", "hpo_id"),
    )
    op.create_table(
        "participant",
        sa.Column("participant_id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("version", sa.Integer(), nullable=False),
        sa.Column("biobank_id", sa.Integer(), nullable=False),
        sa.Column("last_modified", model.utils.UTCDateTime(), nullable=False),
        sa.Column("sign_up_time", model.utils.UTCDateTime(), nullable=False),
        sa.Column("provider_link", sa.BLOB(), nullable=True),
        sa.Column("client_id", sa.String(length=80), nullable=True),
        sa.Column("withdrawal_status", model.utils.Enum(WithdrawalStatus), nullable=False),
        sa.Column("withdrawal_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("suspension_status", model.utils.Enum(SuspensionStatus), nullable=False),
        sa.Column("suspension_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("hpo_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["hpo_id"], ["hpo.hpo_id"]),
        sa.PrimaryKeyConstraint("participant_id"),
    )
    op.create_index("participant_biobank_id", "participant", ["biobank_id"], unique=True)
    op.create_index("participant_hpo_id", "participant", ["hpo_id"], unique=False)
    op.create_table(
        "participant_history",
        sa.Column("participant_id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("biobank_id", sa.Integer(), nullable=False),
        sa.Column("last_modified", model.utils.UTCDateTime(), nullable=False),
        sa.Column("sign_up_time", model.utils.UTCDateTime(), nullable=False),
        sa.Column("provider_link", sa.BLOB(), nullable=True),
        sa.Column("client_id", sa.String(length=80), nullable=True),
        sa.Column("withdrawal_status", model.utils.Enum(WithdrawalStatus), nullable=False),
        sa.Column("withdrawal_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("suspension_status", model.utils.Enum(SuspensionStatus), nullable=False),
        sa.Column("suspension_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("version", sa.Integer(), nullable=False),
        sa.Column("hpo_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["hpo_id"], ["hpo.hpo_id"]),
        sa.PrimaryKeyConstraint("participant_id", "version"),
    )
    op.create_table(
        "biobank_order",
        sa.Column("biobank_order_id", sa.String(length=80), nullable=False),
        sa.Column("participant_id", sa.Integer(), nullable=False),
        sa.Column("log_position_id", sa.Integer(), nullable=False),
        sa.Column("source_site_system", sa.String(length=80), nullable=True),
        sa.Column("source_site_value", sa.String(length=80), nullable=True),
        sa.Column("created", model.utils.UTCDateTime(), nullable=False),
        sa.Column("collected_note", sa.UnicodeText(), nullable=True),
        sa.Column("processed_note", sa.UnicodeText(), nullable=True),
        sa.Column("finalized_note", sa.UnicodeText(), nullable=True),
        sa.ForeignKeyConstraint(["log_position_id"], ["log_position.log_position_id"]),
        sa.ForeignKeyConstraint(["participant_id"], ["participant.participant_id"]),
        sa.PrimaryKeyConstraint("biobank_order_id"),
    )
    op.create_table(
        "biobank_stored_sample",
        sa.Column("biobank_stored_sample_id", sa.String(length=80), nullable=False),
        sa.Column("biobank_id", sa.Integer(), nullable=True),
        sa.Column("test", sa.String(length=80), nullable=False),
        sa.Column("confirmed", model.utils.UTCDateTime(), nullable=True),
        sa.ForeignKeyConstraint(["biobank_id"], ["participant.biobank_id"]),
        sa.PrimaryKeyConstraint("biobank_stored_sample_id"),
    )
    op.create_table(
        "code_history",
        sa.Column("system", sa.String(length=255), nullable=False),
        sa.Column("value", sa.String(length=80), nullable=False),
        sa.Column("display", sa.UnicodeText(), nullable=True),
        sa.Column("topic", sa.UnicodeText(), nullable=True),
        sa.Column("code_type", model.utils.Enum(CodeType), nullable=False),
        sa.Column("mapped", sa.Boolean(), nullable=False),
        sa.Column("created", model.utils.UTCDateTime(), nullable=False),
        sa.Column("code_history_id", sa.Integer(), nullable=False),
        sa.Column("code_id", sa.Integer(), nullable=True),
        sa.Column("code_book_id", sa.Integer(), nullable=True),
        sa.Column("parent_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["code_book_id"], ["code_book.code_book_id"]),
        sa.ForeignKeyConstraint(["parent_id"], ["code.code_id"]),
        sa.PrimaryKeyConstraint("code_history_id"),
        sa.UniqueConstraint("code_book_id", "code_id"),
        sa.UniqueConstraint("code_book_id", "system", "value"),
    )
    op.create_table(
        "participant_summary",
        sa.Column("participant_id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("biobank_id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(length=80), nullable=False),
        sa.Column("middle_name", sa.String(length=80), nullable=True),
        sa.Column("last_name", sa.String(length=80), nullable=False),
        sa.Column("zip_code", sa.String(length=10), nullable=True),
        sa.Column("state_id", sa.Integer(), nullable=True),
        sa.Column("city", sa.String(length=80), nullable=True),
        sa.Column("street_address", sa.String(length=255), nullable=True),
        sa.Column("phone_number", sa.String(length=80), nullable=True),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("recontact_method_id", sa.Integer(), nullable=True),
        sa.Column("language_id", sa.Integer(), nullable=True),
        sa.Column("date_of_birth", sa.Date(), nullable=True),
        sa.Column("gender_identity_id", sa.Integer(), nullable=True),
        sa.Column("sex_id", sa.Integer(), nullable=True),
        sa.Column("sexual_orientation_id", sa.Integer(), nullable=True),
        sa.Column("education_id", sa.Integer(), nullable=True),
        sa.Column("income_id", sa.Integer(), nullable=True),
        sa.Column("enrollment_status", model.utils.Enum(EnrollmentStatus), nullable=True),
        sa.Column("race", model.utils.Enum(Race), nullable=True),
        sa.Column("physical_measurements_status", model.utils.Enum(PhysicalMeasurementsStatus), nullable=True),
        sa.Column("physical_measurements_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("sign_up_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("hpo_id", sa.Integer(), nullable=False),
        sa.Column("consent_for_study_enrollment", model.utils.Enum(QuestionnaireStatus), nullable=True),
        sa.Column("consent_for_study_enrollment_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("consent_for_electronic_health_records", model.utils.Enum(QuestionnaireStatus), nullable=True),
        sa.Column("consent_for_electronic_health_records_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("questionnaire_on_overall_health", model.utils.Enum(QuestionnaireStatus), nullable=True),
        sa.Column("questionnaire_on_overall_health_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("questionnaire_on_lifestyle", model.utils.Enum(QuestionnaireStatus), nullable=True),
        sa.Column("questionnaire_on_lifestyle_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("questionnaire_on_the_basics", model.utils.Enum(QuestionnaireStatus), nullable=True),
        sa.Column("questionnaire_on_the_basics_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("questionnaire_on_healthcare_access", model.utils.Enum(QuestionnaireStatus), nullable=True),
        sa.Column("questionnaire_on_healthcare_access_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("questionnaire_on_medical_history", model.utils.Enum(QuestionnaireStatus), nullable=True),
        sa.Column("questionnaire_on_medical_history_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("questionnaire_on_medications", model.utils.Enum(QuestionnaireStatus), nullable=True),
        sa.Column("questionnaire_on_medications_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("questionnaire_on_family_health", model.utils.Enum(QuestionnaireStatus), nullable=True),
        sa.Column("questionnaire_on_family_health_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("sample_status_1sst8", model.utils.Enum(SampleStatus), nullable=True),
        sa.Column("sample_status_1sst8_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("sample_status_1pst8", model.utils.Enum(SampleStatus), nullable=True),
        sa.Column("sample_status_1pst8_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("sample_status_1hep4", model.utils.Enum(SampleStatus), nullable=True),
        sa.Column("sample_status_1hep4_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("sample_status_1ed04", model.utils.Enum(SampleStatus), nullable=True),
        sa.Column("sample_status_1ed04_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("sample_status_1ed10", model.utils.Enum(SampleStatus), nullable=True),
        sa.Column("sample_status_1ed10_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("sample_status_2ed10", model.utils.Enum(SampleStatus), nullable=True),
        sa.Column("sample_status_2ed10_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("sample_status_1ur10", model.utils.Enum(SampleStatus), nullable=True),
        sa.Column("sample_status_1ur10_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("sample_status_1sal", model.utils.Enum(SampleStatus), nullable=True),
        sa.Column("sample_status_1sal_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("num_completed_baseline_ppi_modules", sa.SmallInteger(), nullable=True),
        sa.Column("num_completed_ppi_modules", sa.SmallInteger(), nullable=True),
        sa.Column("num_baseline_samples_arrived", sa.SmallInteger(), nullable=True),
        sa.Column("samples_to_isolate_dna", model.utils.Enum(SampleStatus), nullable=True),
        sa.Column("withdrawal_status", model.utils.Enum(WithdrawalStatus), nullable=False),
        sa.Column("withdrawal_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("suspension_status", model.utils.Enum(SuspensionStatus), nullable=False),
        sa.Column("suspension_time", model.utils.UTCDateTime(), nullable=True),
        sa.ForeignKeyConstraint(["education_id"], ["code.code_id"]),
        sa.ForeignKeyConstraint(["gender_identity_id"], ["code.code_id"]),
        sa.ForeignKeyConstraint(["hpo_id"], ["hpo.hpo_id"]),
        sa.ForeignKeyConstraint(["income_id"], ["code.code_id"]),
        sa.ForeignKeyConstraint(["language_id"], ["code.code_id"]),
        sa.ForeignKeyConstraint(["participant_id"], ["participant.participant_id"]),
        sa.ForeignKeyConstraint(["recontact_method_id"], ["code.code_id"]),
        sa.ForeignKeyConstraint(["sex_id"], ["code.code_id"]),
        sa.ForeignKeyConstraint(["sexual_orientation_id"], ["code.code_id"]),
        sa.ForeignKeyConstraint(["state_id"], ["code.code_id"]),
        sa.PrimaryKeyConstraint("participant_id"),
    )
    op.create_index("participant_summary_biobank_id", "participant_summary", ["biobank_id"], unique=False)
    op.create_index("participant_summary_hpo", "participant_summary", ["hpo_id"], unique=False)
    op.create_index(
        "participant_summary_hpo_consent",
        "participant_summary",
        ["hpo_id", "consent_for_study_enrollment"],
        unique=False,
    )
    op.create_index("participant_summary_hpo_dob", "participant_summary", ["hpo_id", "date_of_birth"], unique=False)
    op.create_index("participant_summary_hpo_fn", "participant_summary", ["hpo_id", "first_name"], unique=False)
    op.create_index("participant_summary_hpo_ln", "participant_summary", ["hpo_id", "last_name"], unique=False)
    op.create_index(
        "participant_summary_hpo_num_baseline_ppi",
        "participant_summary",
        ["hpo_id", "num_completed_baseline_ppi_modules"],
        unique=False,
    )
    op.create_index(
        "participant_summary_hpo_num_baseline_samples",
        "participant_summary",
        ["hpo_id", "num_baseline_samples_arrived"],
        unique=False,
    )
    op.create_index("participant_summary_hpo_race", "participant_summary", ["hpo_id", "race"], unique=False)
    op.create_index(
        "participant_summary_hpo_status", "participant_summary", ["hpo_id", "enrollment_status"], unique=False
    )
    op.create_index(
        "participant_summary_hpo_withdrawal_status_time",
        "participant_summary",
        ["hpo_id", "withdrawal_status", "withdrawal_time"],
        unique=False,
    )
    op.create_index("participant_summary_hpo_zip", "participant_summary", ["hpo_id", "zip_code"], unique=False)
    op.create_index("participant_summary_ln_dob", "participant_summary", ["last_name", "date_of_birth"], unique=False)
    op.create_index(
        "participant_summary_ln_dob_fn",
        "participant_summary",
        ["last_name", "date_of_birth", "first_name"],
        unique=False,
    )
    op.create_index(
        "participant_summary_ln_dob_zip",
        "participant_summary",
        ["last_name", "date_of_birth", "zip_code"],
        unique=False,
    )
    op.create_table(
        "physical_measurements",
        sa.Column("physical_measurements_id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("participant_id", sa.Integer(), nullable=False),
        sa.Column("created", model.utils.UTCDateTime(), nullable=False),
        sa.Column("resource", sa.BLOB(), nullable=False),
        sa.Column("final", sa.Boolean(), nullable=False),
        sa.Column("amended_measurements_id", sa.Integer(), nullable=True),
        sa.Column("log_position_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["amended_measurements_id"], ["physical_measurements.physical_measurements_id"]),
        sa.ForeignKeyConstraint(["log_position_id"], ["log_position.log_position_id"]),
        sa.ForeignKeyConstraint(["participant_id"], ["participant.participant_id"]),
        sa.PrimaryKeyConstraint("physical_measurements_id"),
    )
    op.create_table(
        "questionnaire_concept",
        sa.Column("questionnaire_concept_id", sa.Integer(), nullable=False),
        sa.Column("questionnaire_id", sa.Integer(), nullable=False),
        sa.Column("questionnaire_version", sa.Integer(), nullable=False),
        sa.Column("code_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["code_id"], ["code.code_id"]),
        sa.ForeignKeyConstraint(
            ["questionnaire_id", "questionnaire_version"],
            ["questionnaire_history.questionnaire_id", "questionnaire_history.version"],
        ),
        sa.PrimaryKeyConstraint("questionnaire_concept_id"),
        sa.UniqueConstraint("questionnaire_id", "questionnaire_version", "code_id"),
    )
    op.create_table(
        "questionnaire_question",
        sa.Column("questionnaire_question_id", sa.Integer(), nullable=False),
        sa.Column("questionnaire_id", sa.Integer(), nullable=True),
        sa.Column("questionnaire_version", sa.Integer(), nullable=True),
        sa.Column("link_id", sa.String(length=20), nullable=True),
        sa.Column("code_id", sa.Integer(), nullable=False),
        sa.Column("repeats", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(["code_id"], ["code.code_id"]),
        sa.ForeignKeyConstraint(
            ["questionnaire_id", "questionnaire_version"],
            ["questionnaire_history.questionnaire_id", "questionnaire_history.version"],
        ),
        sa.PrimaryKeyConstraint("questionnaire_question_id"),
        sa.UniqueConstraint("questionnaire_id", "questionnaire_version", "link_id"),
    )
    op.create_table(
        "questionnaire_response",
        sa.Column("questionnaire_response_id", sa.Integer(), autoincrement=False, nullable=False),
        sa.Column("questionnaire_id", sa.Integer(), nullable=False),
        sa.Column("questionnaire_version", sa.Integer(), nullable=False),
        sa.Column("participant_id", sa.Integer(), nullable=False),
        sa.Column("created", model.utils.UTCDateTime(), nullable=False),
        sa.Column("resource", sa.BLOB(), nullable=False),
        sa.ForeignKeyConstraint(["participant_id"], ["participant.participant_id"]),
        sa.ForeignKeyConstraint(
            ["questionnaire_id", "questionnaire_version"],
            ["questionnaire_history.questionnaire_id", "questionnaire_history.version"],
        ),
        sa.PrimaryKeyConstraint("questionnaire_response_id"),
    )
    op.create_table(
        "biobank_order_identifier",
        sa.Column("system", sa.String(length=80), nullable=False),
        sa.Column("value", sa.String(length=80), nullable=False),
        sa.Column("biobank_order_id", sa.String(length=80), nullable=False),
        sa.ForeignKeyConstraint(["biobank_order_id"], ["biobank_order.biobank_order_id"]),
        sa.PrimaryKeyConstraint("system", "value"),
    )
    op.create_table(
        "biobank_ordered_sample",
        sa.Column("order_id", sa.String(length=80), nullable=False),
        sa.Column("test", sa.String(length=80), nullable=False),
        sa.Column("description", sa.UnicodeText(), nullable=False),
        sa.Column("processing_required", sa.Boolean(), nullable=False),
        sa.Column("collected", model.utils.UTCDateTime(), nullable=True),
        sa.Column("processed", model.utils.UTCDateTime(), nullable=True),
        sa.Column("finalized", model.utils.UTCDateTime(), nullable=True),
        sa.ForeignKeyConstraint(["order_id"], ["biobank_order.biobank_order_id"]),
        sa.PrimaryKeyConstraint("order_id", "test"),
    )
    op.create_table(
        "questionnaire_response_answer",
        sa.Column("questionnaire_response_answer_id", sa.Integer(), nullable=False),
        sa.Column("questionnaire_response_id", sa.Integer(), nullable=False),
        sa.Column("question_id", sa.Integer(), nullable=False),
        sa.Column("end_time", model.utils.UTCDateTime(), nullable=True),
        sa.Column("value_system", sa.String(length=50), nullable=True),
        sa.Column("value_code_id", sa.Integer(), nullable=True),
        sa.Column("value_boolean", sa.Boolean(), nullable=True),
        sa.Column("value_decimal", sa.Float(), nullable=True),
        sa.Column("value_integer", sa.Integer(), nullable=True),
        sa.Column("value_string", sa.String(length=1024), nullable=True),
        sa.Column("value_date", sa.Date(), nullable=True),
        sa.Column("value_datetime", model.utils.UTCDateTime(), nullable=True),
        sa.ForeignKeyConstraint(["question_id"], ["questionnaire_question.questionnaire_question_id"]),
        sa.ForeignKeyConstraint(["questionnaire_response_id"], ["questionnaire_response.questionnaire_response_id"]),
        sa.ForeignKeyConstraint(["value_code_id"], ["code.code_id"]),
        sa.PrimaryKeyConstraint("questionnaire_response_answer_id"),
    )
    # ### end Alembic commands ###


def downgrade_rdr():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("questionnaire_response_answer")
    op.drop_table("biobank_ordered_sample")
    op.drop_table("biobank_order_identifier")
    op.drop_table("questionnaire_response")
    op.drop_table("questionnaire_question")
    op.drop_table("questionnaire_concept")
    op.drop_table("physical_measurements")
    op.drop_index("participant_summary_ln_dob_zip", table_name="participant_summary")
    op.drop_index("participant_summary_ln_dob_fn", table_name="participant_summary")
    op.drop_index("participant_summary_ln_dob", table_name="participant_summary")
    op.drop_index("participant_summary_hpo_zip", table_name="participant_summary")
    op.drop_index("participant_summary_hpo_withdrawal_status_time", table_name="participant_summary")
    op.drop_index("participant_summary_hpo_status", table_name="participant_summary")
    op.drop_index("participant_summary_hpo_race", table_name="participant_summary")
    op.drop_index("participant_summary_hpo_num_baseline_samples", table_name="participant_summary")
    op.drop_index("participant_summary_hpo_num_baseline_ppi", table_name="participant_summary")
    op.drop_index("participant_summary_hpo_ln", table_name="participant_summary")
    op.drop_index("participant_summary_hpo_fn", table_name="participant_summary")
    op.drop_index("participant_summary_hpo_dob", table_name="participant_summary")
    op.drop_index("participant_summary_hpo_consent", table_name="participant_summary")
    op.drop_index("participant_summary_hpo", table_name="participant_summary")
    op.drop_index("participant_summary_biobank_id", table_name="participant_summary")
    op.drop_table("participant_summary")
    op.drop_table("code_history")
    op.drop_table("biobank_stored_sample")
    op.drop_table("biobank_order")
    op.drop_table("participant_history")
    op.drop_index("participant_hpo_id", table_name="participant")
    op.drop_index("participant_biobank_id", table_name="participant")
    op.drop_table("participant")
    op.drop_table("metrics_bucket")
    op.drop_table("code")
    op.drop_table("questionnaire_history")
    op.drop_table("questionnaire")
    op.drop_table("metrics_version")
    op.drop_table("log_position")
    op.drop_table("hpo")
    op.drop_table("code_book")
    # ### end Alembic commands ###
