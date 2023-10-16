from fastapi import APIRouter
from .message import message_router

# router for public API v1
v1_router = APIRouter()

v1_router.include_router(message_router)
