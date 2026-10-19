from httpx import AsyncClient
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.hello.models import HelloMessage
from app.modules.hello.service import get_greeting


async def test_hello_returns_greeting(client: AsyncClient) -> None:
    response = await client.get("/api/v1/hello")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world"}


async def test_get_greeting_inserts_once(session: AsyncSession) -> None:
    first = await get_greeting(session)
    second = await get_greeting(session)

    count = await session.scalar(select(func.count()).select_from(HelloMessage))
    assert first.id == second.id
    assert first.message == "Hello, world"
    assert count == 1
