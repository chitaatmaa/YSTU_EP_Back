"""Drop unique constraints from disciplines name/short_name

Revision ID: 20260527_drop_unique_disciplines
Revises: 781d429959a3
Create Date: 2026-05-27
"""

from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "20260527_drop_unique_disciplines"
down_revision: Union[str, None] = "781d429959a3"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Default Postgres naming for unnamed unique constraints:
    # - disciplines.name      -> disciplines_name_key
    # - disciplines.short_name-> disciplines_short_name_key
    op.drop_constraint("disciplines_name_key", "disciplines", type_="unique")
    op.drop_constraint("disciplines_short_name_key", "disciplines", type_="unique")


def downgrade() -> None:
    op.create_unique_constraint("disciplines_name_key", "disciplines", ["name"])
    op.create_unique_constraint("disciplines_short_name_key", "disciplines", ["short_name"])

