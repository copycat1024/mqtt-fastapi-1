from tortoise import run_async
from util.log import create_logger
from .db import generate_schema

logger = create_logger('api')

if __name__ == "__main__":
    logger.info("Creating schema ...")
    run_async(generate_schema())
    logger.info("Creating schema done.")
