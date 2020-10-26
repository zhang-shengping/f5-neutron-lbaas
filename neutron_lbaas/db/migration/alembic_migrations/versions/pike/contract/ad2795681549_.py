# Copyright 2020 <PUT YOUR NAME/COMPANY HERE>
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""empty message

Revision ID: ad2795681549
Revises: e6417a8b114d
Create Date: 2020-10-26 01:22:03.300857

"""

# revision identifiers, used by Alembic.
revision = 'ad2795681549'
down_revision = 'e6417a8b114d'

from alembic import op
import sqlalchemy as sa

from neutron.db import migration

old_listener_protocols = sa.Enum("HTTP", "HTTPS", "TCP", "TERMINATED_HTTPS",
                             name="listener_protocolsv2")

new_listener_protocols = sa.Enum("HTTP", "HTTPS", "TCP", "TERMINATED_HTTPS", "FTP",
                             name="listener_protocolsv2")

def upgrade():
    migration.alter_enum(
        'lbaas_listeners',
        'protocol', 
        new_listener_protocols,
        nullable=False
    )
# def upgrade():
#     sa.alter_column(
#         'lbaas_listeners',
#         'protocol', 
#         new_listener_protocols,
#         existing_type=old_listener_protocols,
#         existing_nullable=nullable
#     )
