import logging
import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from api.route import v1_router, private_router
from api.middleware import HttpLog


def create_application() -> FastAPI:
    # create the FastAPI application
    logger = logging.getLogger("api")
    application = FastAPI(title="Message REST", version="1.0")

    # mount the router
    application.include_router(private_router)
    application.include_router(v1_router)

    # mount the middleware
    application.add_middleware(HttpLog)

    # hook up startup event
    @application.on_event("startup")
    async def startup_event() -> None:
        logger.info(f"Initialing database url ...")
        register_tortoise(
            app,
            db_url=os.getenv("DB_URL"),
            modules={"models": ["db.model"]},
        )
        logger.info("Database initialization done.")

    # hook up shutdown event
    @application.on_event("shutdown")
    async def shutdown_event() -> None:
        logger.info("Shutting down...")

    return application


app = create_application()
