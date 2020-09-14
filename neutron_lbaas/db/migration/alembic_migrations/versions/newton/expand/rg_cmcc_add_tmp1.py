from alembic import op
import sqlalchemy as sa

from neutron.db import migration


# revision identifiers, used by Alembic.
revision = 'rg_cmcc_v0.1'
down_revision = 'rg_cmcc'


# milestone identifier, used by neutron-db-manage
neutron_milestone = [migration.NEWTON]


def upgrade():

    # listeners
    op.add_column('lbaas_listeners', sa.Column(
        u'redirect_up', sa.Boolean(), nullable=True
    ))
    op.add_column('lbaas_listeners', sa.Column(
        u'mutual_authentication_up', sa.Boolean(), nullable=True
    ))
