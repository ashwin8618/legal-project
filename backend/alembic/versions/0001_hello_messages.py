"""create hello messages and enable pgvector

Revision ID: 0001_hello
Revises:
Create Date: 2026-10-19

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "0001_hello"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS vector")
    op.create_table(
        "hello_messages",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("message", sa.String(length=255), nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_table("hello_messages")
    op.execute("DROP EXTENSION IF EXISTS vector")
