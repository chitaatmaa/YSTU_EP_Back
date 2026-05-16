"""Add has_course_work to discipline_blocks table

Revision ID: 20260515_add_has_course_work
Revises: 20251210_add_calendar_plan.py
Create Date: 2026-05-15

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '20260515_add_has_course_work'
down_revision: Union[str, None] = '20251210_add_calendar_plan.py'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('discipline_blocks', sa.Column('has_course_work', sa.Boolean(), nullable=False, server_default='false'))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('discipline_blocks', 'has_course_work')
