import os
from tortoise import Tortoise


async def generate_schema() -> None:
    await Tortoise.init(
        db_url=os.getenv("DB_URL"),
        modules={"models": ["db.model"]},
    )
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()
