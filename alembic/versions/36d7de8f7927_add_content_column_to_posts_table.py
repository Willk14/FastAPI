"""add content column to posts table

Revision ID: 36d7de8f7927
Revises: 0357d4f89816
Create Date: 2025-01-27 12:34:08.792220

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '36d7de8f7927'
down_revision: Union[str, None] = '0357d4f89816'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
