from alembic import op
import sqlalchemy as sa

from neutron.db import migration


# revision identifiers, used by Alembic.
revision = 'rg_cmcc'
down_revision = '844352f9fe6f'


# milestone identifier, used by neutron-db-manage
neutron_milestone = [migration.NEWTON]


def upgrade():
    # memeber
    op.add_column('lbaas_members', sa.Column(
        u'bandwidth', sa.Integer(), nullable=True))

    # listeners
    op.add_column('lbaas_listeners', sa.Column(
        u'redirect', sa.Boolean(), nullable=True
    ))
    op.add_column('lbaas_listeners', sa.Column(
        u'redirect_protocol', sa.String(36), nullable=True
    ))
    op.add_column('lbaas_listeners', sa.Column(
        u'redirect_port', sa.Integer(), nullable=True
    ))
    op.add_column('lbaas_listeners', sa.Column(
        u'mutual_authentication_u', sa.Boolean(), nullable=True
    ))
    op.add_column('lbaas_listeners', sa.Column(
        u'ca_container_id', sa.String(36), nullable=True
    ))