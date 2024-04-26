"""adding_p5_raw

Revision ID: 77641d359c1a
Revises: 6b8cc85c5389
Create Date: 2024-04-26 09:23:00.830927

"""
from alembic import op
import sqlalchemy as sa
import rdr_service.model.utils
from sqlalchemy.dialects import mysql

from rdr_service.participant_enums import PhysicalMeasurementsStatus, QuestionnaireStatus, OrderStatus
from rdr_service.participant_enums import WithdrawalStatus, WithdrawalReason, SuspensionStatus, QuestionnaireDefinitionStatus
from rdr_service.participant_enums import EnrollmentStatus, Race, SampleStatus, OrganizationType, BiobankOrderStatus
from rdr_service.participant_enums import OrderShipmentTrackingStatus, OrderShipmentStatus
from rdr_service.participant_enums import MetricSetType, MetricsKey, GenderIdentity
from rdr_service.model.base import add_table_history_table, drop_table_history_table
from rdr_service.model.code import CodeType
from rdr_service.model.site_enums import SiteStatus, EnrollingStatus, DigitalSchedulingStatus, ObsoleteStatus

# revision identifiers, used by Alembic.
revision = '77641d359c1a'
down_revision = '6b8cc85c5389'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()


def upgrade_rdr():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genomic_p5_raw',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('file_path', sa.String(length=255), nullable=True),
    sa.Column('ignore_flag', sa.SmallInteger(), nullable=False),
    sa.Column('biobank_id', sa.String(length=255), nullable=True),
    sa.Column('sample_id', sa.String(length=255), nullable=True),
    sa.Column('biobankid_sampleid', sa.String(length=255), nullable=True),
    sa.Column('sex_at_birth', sa.String(length=255), nullable=True),
    sa.Column('site_id', sa.String(length=255), nullable=True),
    sa.Column('npx_explore_path', sa.String(length=255), nullable=True),
    sa.Column('analysis_report_path', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_genomic_p5_raw_biobank_id'), 'genomic_p5_raw', ['biobank_id'], unique=False)
    op.create_index(op.f('ix_genomic_p5_raw_file_path'), 'genomic_p5_raw', ['file_path'], unique=False)
    op.create_index(op.f('ix_genomic_p5_raw_sample_id'), 'genomic_p5_raw', ['sample_id'], unique=False)
    # ### end Alembic commands ###


def downgrade_rdr():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_genomic_p5_raw_sample_id'), table_name='genomic_p5_raw')
    op.drop_index(op.f('ix_genomic_p5_raw_file_path'), table_name='genomic_p5_raw')
    op.drop_index(op.f('ix_genomic_p5_raw_biobank_id'), table_name='genomic_p5_raw')
    op.drop_table('genomic_p5_raw')
    # ### end Alembic commands ###


def upgrade_metrics():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_metrics():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

