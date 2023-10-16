from fastapi import FastAPI, Query, HTTPException, Request
from tortoise.contrib.fastapi import register_tortoise
from db.model import Message as DbMessage
from util.model import Message
import logging
from typing import Annotated

DB_URL = "postgres://webster:pass123@db:5432/backend"


def create_application() -> FastAPI:
    logger = logging.getLogger("api")
    application = FastAPI(title="MQTT - FastAPI", version="0.1.0")

    @application.on_event("startup")
    async def startup_event() -> None:
        logger.info("Initialing database...")
        register_tortoise(
            app,
            db_url=DB_URL,
            modules={"models": ["db.model"]},
        )
        logger.info("Database initialization done.")

    @application.on_event("shutdown")
    async def shutdown_event() -> None:
        logger.info("Shutting down...")

    @application.get("/")
    async def root():
        return {"message": "Hello World"}

    @application.get("/v1/messages")
    async def read_all_messages(
        limit: Annotated[int, Query(ge=0)] = 100,
        offset: Annotated[int, Query(ge=0)] = 0,
    ) -> list[Message]:
        try:
            return [
                Message(
                    created_at=msg.created_at,
                    charger_id=msg.charger_id,
                    connector_id=msg.connector_id,
                    session_id=msg.session_id,
                    payload=msg.payload,
                )
                async for msg in DbMessage.all().limit(limit).offset(offset)
            ]

        except Exception as e:
            logger.info(e)
            raise HTTPException(status_code=500, detail="Internal server error")

    @application.middleware("http")
    async def log_requests(request: Request, call_next):
        header = f"{request.method} {request.url.path}"
        logger.info(f"{header} processing...")

        response = await call_next(request)

        logger.info(f"{header} done.")

        return response

    return application


app = create_application()
