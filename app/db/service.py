from .model import Message as DbMessage
from dataclass.model import Message
import logging


logger = logging.getLogger("api")


async def save_msg(msg: Message) -> None:
    try:
        await DbMessage(
            created_at=msg.created_at,
            charger_id=msg.charger_id,
            connector_id=msg.connector_id,
            session_id=msg.session_id,
            payload=msg.payload,
        ).save()

    except Exception as e:
        logger.error(e)


async def read_msg(limit: int, offset: int) -> list[Message]:
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
