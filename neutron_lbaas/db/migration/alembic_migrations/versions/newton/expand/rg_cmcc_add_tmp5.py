from alembic import op
import sqlalchemy as sa

from neutron.db import migration


# revision identifiers, used by Alembic.
revision = 'rg_cmcc_v0.5'
down_revision = 'rg_cmcc_v0.4'


# milestone identifier, used by neutron-db-managerg_cmcc_add_tmp3.py
neutron_milestone = [migration.NEWTON]


def upgrade():
    op.add_column('lbaas_members', sa.Column(
        u'member_status', sa.String(16), nullable=False))
