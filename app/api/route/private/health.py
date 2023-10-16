from fastapi import APIRouter


health_router = APIRouter()


@health_router.get("/health_check")
async def health_check() -> dict[str, str]:
    return {"message": "OK"}
