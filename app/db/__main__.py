from tortoise import run_async
from .db import generate_schema

if __name__ == "__main__":
    run_async(generate_schema())
