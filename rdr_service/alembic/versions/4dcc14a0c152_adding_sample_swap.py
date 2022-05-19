"""adding_sample_swap

Revision ID: 4dcc14a0c152
Revises: dab3d1576991, 6460d98c775e
Create Date: 2022-05-17 14:10:14.511703

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4dcc14a0c152'
down_revision = ('dab3d1576991', '6460d98c775e')
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()


def upgrade_rdr():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genomic_sample_swap',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('explanation', sa.String(length=512), nullable=True),
    sa.Column('open_investigation', sa.SmallInteger(), nullable=False),
    sa.Column('open_investigation_date', sa.DateTime(), nullable=True),
    sa.Column('closed_investigation', sa.DateTime(), nullable=True),
    sa.Column('closed_investigation_date', sa.DateTime(), nullable=True),
    sa.Column('ignore_flag', sa.SmallInteger(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('genomic_sample_swap_member',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('genomic_sample_swap', sa.Integer(), nullable=False),
    sa.Column('genomic_set_member_id', sa.Integer(), nullable=False),
    sa.Column('ignore_flag', sa.SmallInteger(), nullable=False),
    sa.ForeignKeyConstraint(['genomic_sample_swap'], ['genomic_sample_swap.id'], ),
    sa.ForeignKeyConstraint(['genomic_set_member_id'], ['genomic_set_member.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.add_column('genomic_informing_loop', sa.Column('sample_id', sa.String(length=80), nullable=True))
    op.create_index(op.f('ix_genomic_informing_loop_sample_id'), 'genomic_informing_loop', ['sample_id'], unique=False)
    op.add_column('genomic_result_viewed', sa.Column('sample_id', sa.String(length=80), nullable=True))
    op.create_index(op.f('ix_genomic_result_viewed_sample_id'), 'genomic_result_viewed', ['sample_id'], unique=False)
    # ### end Alembic commands ###

    op.execute(
        """
        Update genomic_informing_loop gil
        Inner join genomic_set_member gsm
            On gsm.participant_id = gil.participant_id
        Set gil.sample_id = gsm.sample_id
        Where gsm.genome_type = 'aou_array'
        And gil.module_type = 'gem'
        """
    )

    op.execute(
        """
        Update genomic_result_viewed grv
        Inner join genomic_set_member gsm
            On gsm.participant_id = grv.participant_id
        Set grv.sample_id = gsm.sample_id
        Where gsm.genome_type = 'aou_array'
        And grv.module_type = 'gem'
        """
    )


def downgrade_rdr():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_genomic_result_viewed_sample_id'), table_name='genomic_result_viewed')
    op.drop_column('genomic_result_viewed', 'sample_id')
    op.drop_index(op.f('ix_genomic_informing_loop_sample_id'), table_name='genomic_informing_loop')
    op.drop_column('genomic_informing_loop', 'sample_id')
    op.drop_table('genomic_sample_swap_member')
    op.drop_table('genomic_sample_swap')
    # ### end Alembic commands ###


def upgrade_metrics():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_metrics():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

