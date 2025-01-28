"""add foreign-key to posts table

Revision ID: 6becce5db5b8
Revises: c932c48b13eb
Create Date: 2025-01-27 21:53:18.501888

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6becce5db5b8'
down_revision: Union[str, None] = 'c932c48b13eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
