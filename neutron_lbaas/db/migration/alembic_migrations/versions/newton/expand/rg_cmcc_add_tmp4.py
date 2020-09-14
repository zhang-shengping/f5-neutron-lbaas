from alembic import op
import sqlalchemy as sa

from neutron.db import migration


# revision identifiers, used by Alembic.
revision = 'rg_cmcc_v0.4'
down_revision = 'rg_cmcc_v0.3'


# milestone identifier, used by neutron-db-managerg_cmcc_add_tmp3.py
neutron_milestone = [migration.NEWTON]

listener_protocols = sa.Enum("HTTP", "HTTPS", "TCP", "UDP", "TERMINATED_HTTPS",
                             name="listener_protocolsv2")
pool_protocols = sa.Enum("HTTP", "HTTPS", "TCP", "UDP", "TERMINATED_HTTPS",
                         name="pool_protocolsv2")

def upgrade():
    migration.alter_enum('lbaas_listeners', 'protocol', listener_protocols,
                         nullable=False)

    migration.alter_enum('lbaas_pools', 'protocol', pool_protocols,
                         nullable=False)
