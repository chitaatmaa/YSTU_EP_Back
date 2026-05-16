"""Add is_actual to departments

Revision ID: 20260516_add_is_actual
Revises: 20260515_add_has_course_work
Create Date: 2026-05-16
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20260516_add_is_actual'
down_revision: Union[str, None] = '20260515_add_has_course_work'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('departments', sa.Column('is_actual', sa.Boolean(), nullable=False, server_default=sa.true()))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('departments', 'is_actual')
