"""add content column to posts table

Revision ID: c932c48b13eb
Revises: 0f7d9fd7e8f2
Create Date: 2025-01-27 21:31:18.011477

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c932c48b13eb'
down_revision: Union[str, None] = '0f7d9fd7e8f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
