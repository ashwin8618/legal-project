"""pgvector type used by future embedding modules.

The PostgreSQL extension itself is created in the initial Alembic migration.
"""

from pgvector.sqlalchemy import Vector

__all__ = ["Vector"]
