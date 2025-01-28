"""add phone number

Revision ID: 0ed6cec91630
Revises: adfec2fa4af9
Create Date: 2025-01-27 23:07:41.763140

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ed6cec91630'
down_revision: Union[str, None] = 'adfec2fa4af9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
