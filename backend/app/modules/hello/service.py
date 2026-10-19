from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.hello.models import HelloMessage

DEFAULT_MESSAGE = "Hello, world"


async def get_greeting(session: AsyncSession) -> HelloMessage:
    result = await session.execute(select(HelloMessage).order_by(HelloMessage.id).limit(1))
    greeting = result.scalar_one_or_none()
    if greeting is not None:
        return greeting

    greeting = HelloMessage(message=DEFAULT_MESSAGE)
    session.add(greeting)
    await session.commit()
    await session.refresh(greeting)
    return greeting
