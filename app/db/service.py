from .model import Message as DbMessage
from util.model import Message


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
        print(e)
