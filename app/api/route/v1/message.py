import logging
from typing import Annotated
from fastapi import APIRouter, HTTPException, Query
from dataclass.model import Message
from db.service import read_msg


logger = logging.getLogger("api")
message_router = APIRouter()


@message_router.get("/v1/messages")
async def read_all_messages(
    limit: Annotated[int, Query(ge=0)] = 100,
    offset: Annotated[int, Query(ge=0)] = 0,
) -> list[Message]:
    try:
        return await read_msg(limit, offset)

    except Exception as e:
        logger.info(e)
        raise HTTPException(status_code=500, detail="Internal server error")
