"""add time zone to site

Revision ID: fddd3f850e2c
Revises: 060dba019a3a
Create Date: 2018-01-05 13:32:29.608220

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "fddd3f850e2c"
down_revision = "060dba019a3a"
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()


def upgrade_rdr():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("site", sa.Column("time_zone_id", sa.String(length=1024), nullable=True))
    # ### end Alembic commands ###


def downgrade_rdr():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("site", "time_zone_id")
    # ### end Alembic commands ###


def upgrade_metrics():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_metrics():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
