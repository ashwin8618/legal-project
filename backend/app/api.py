"""Register feature modules on the public HTTP API."""

from fastapi import APIRouter

from app.modules.health.router import router as health_router
from app.modules.hello.router import router as hello_router

api_router = APIRouter(prefix="/api")
api_router.include_router(health_router, tags=["health"])
api_router.include_router(hello_router, prefix="/v1/hello", tags=["hello"])
