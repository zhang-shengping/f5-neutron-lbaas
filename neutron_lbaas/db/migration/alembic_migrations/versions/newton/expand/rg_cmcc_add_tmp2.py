from alembic import op
import sqlalchemy as sa

from neutron.db import migration


# revision identifiers, used by Alembic.
revision = 'rg_cmcc_v0.2'
down_revision = 'rg_cmcc_v0.1'


# milestone identifier, used by neutron-db-manage
neutron_milestone = [migration.NEWTON]

listener_protocols = sa.Enum("HTTP", "HTTPS", "TCP", "UDP", "TERMINATED_HTTPS",
                             name="listener_protocolsv2")
pool_protocols = sa.Enum("HTTP", "HTTPS", "TCP", "UDP", "TERMINATED_HTTPS",
                         name="pool_protocolsv2")

def upgrade():

    op.drop_column(u'lbaas_listeners', 'protocol')
    op.drop_column(u'lbaas_listeners', 'redirect_protocol')
    op.add_column('lbaas_listeners', sa.Column(
        u'redirect_protocol', listener_protocols, nullable=True
    ))
    op.add_column('lbaas_listeners', sa.Column(
        u'protocol', listener_protocols, nullable=True
    ))
    op.drop_column('lbaas_pools', 'protocol')
    op.add_column('lbaas_pools', sa.Column(u'protocol', pool_protocols, nullable=True))
