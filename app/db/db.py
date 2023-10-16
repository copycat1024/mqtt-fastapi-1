from tortoise import Tortoise, run_async

DB_URL = "postgres://webster:pass123@localhost:5400/backend"


async def generate_schema() -> None:
    await Tortoise.init(
        db_url=DB_URL,
        modules={"models": ["db.model"]},
    )
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()
