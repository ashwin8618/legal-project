from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session
from app.modules.hello.schemas import HelloResponse
from app.modules.hello.service import get_greeting

router = APIRouter()


@router.get("", response_model=HelloResponse)
async def read_hello(session: AsyncSession = Depends(get_session)) -> HelloResponse:
    greeting = await get_greeting(session)
    return HelloResponse.model_validate(greeting)
