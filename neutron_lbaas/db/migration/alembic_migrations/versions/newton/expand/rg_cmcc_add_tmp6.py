from alembic import op
import sqlalchemy as sa

from neutron.db import migration


# revision identifiers, used by Alembic.
revision = 'rg_cmcc_v0.6'
down_revision = 'rg_cmcc_v0.5'


# milestone identifier, used by neutron-db-managerg_cmcc_add_tmp3.py
neutron_milestone = [migration.NEWTON]


def upgrade():
    migration.alter_enum('lbaas_listeners', 'ca_container_id', sa.String(128),
                         nullable=False)
