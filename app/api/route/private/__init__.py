from fastapi import APIRouter
from .health import health_router

# router for private API
private_router = APIRouter()
private_router.include_router(health_router)
