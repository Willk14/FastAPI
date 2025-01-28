"""add user table

Revision ID: 0f7d9fd7e8f2
Revises: 36d7de8f7927
Create Date: 2025-01-27 12:58:25.423365

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f7d9fd7e8f2'
down_revision: Union[str, None] = '36d7de8f7927'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
