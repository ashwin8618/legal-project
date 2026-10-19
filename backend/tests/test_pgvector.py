from pgvector.sqlalchemy import Vector

from app.core.pgvector import Vector as AppVector


def test_pgvector_type_is_available() -> None:
    column_type = AppVector(3)

    assert isinstance(column_type, Vector)
    assert column_type.dim == 3
