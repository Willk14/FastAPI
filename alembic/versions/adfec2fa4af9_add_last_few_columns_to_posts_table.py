"""add last few columns to posts table

Revision ID: adfec2fa4af9
Revises: 6becce5db5b8
Create Date: 2025-01-27 22:05:50.785160

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'adfec2fa4af9'
down_revision: Union[str, None] = '6becce5db5b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')
    ))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'craeted_at')
    pass
