from alembic import op
import sqlalchemy as sa

from neutron.db import migration


# revision identifiers, used by Alembic.
revision = 'rg_cmcc_v0.3'
down_revision = 'rg_cmcc_v0.2'


# milestone identifier, used by neutron-db-managerg_cmcc_add_tmp3.py
neutron_milestone = [migration.NEWTON]

def upgrade():

    op.drop_column(u'lbaas_members', 'bandwidth')
    op.add_column('lbaas_loadbalancers', sa.Column(
        u'bandwidth', sa.Integer(), nullable=True
    ))

