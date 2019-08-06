"""Update order columns

Revision ID: d3bcbe963bf0
Revises: d5cb0d93b970
Create Date: 2017-05-12 15:05:12.807535

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "d3bcbe963bf0"
down_revision = "d5cb0d93b970"
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
    op.add_column("biobank_order", sa.Column("finalized_site_id", sa.Integer(), nullable=True))
    op.add_column("biobank_order", sa.Column("finalized_username", sa.String(length=255), nullable=True))
    op.add_column("biobank_order", sa.Column("source_site_id", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "biobank_order", "site", ["finalized_site_id"], ["site_id"])
    op.create_foreign_key(None, "biobank_order", "site", ["source_site_id"], ["site_id"])
    op.drop_column("biobank_order", "source_site_value")
    op.drop_column("biobank_order", "source_site_system")
    # ### end Alembic commands ###


def downgrade_rdr():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("biobank_order", sa.Column("source_site_system", mysql.VARCHAR(length=80), nullable=True))
    op.add_column("biobank_order", sa.Column("source_site_value", mysql.VARCHAR(length=80), nullable=True))
    op.drop_constraint(None, "biobank_order", type_="foreignkey")
    op.drop_constraint(None, "biobank_order", type_="foreignkey")
    op.drop_column("biobank_order", "source_site_id")
    op.drop_column("biobank_order", "finalized_username")
    op.drop_column("biobank_order", "finalized_site_id")
    # ### end Alembic commands ###
