from datetime import datetime
from .filter import Filter
from dataclass.model import Message
from db.service import save_msg
from util.log import create_logger


logger = create_logger("mqtt")


class SessionFilter(Filter):
    pattern = r"charger/(\d+)/connector/(\d+)/session/(\d+)"

    async def handle(self, payload, charger_id, connector_id, session_id):
        # create new message item
        message = Message(
            created_at=datetime.now(),
            charger_id=charger_id,
            connector_id=connector_id,
            session_id=session_id,
            payload=payload,
        )
        logger.info(f"Subscriber received: {message}")

        # save message to database
        await save_msg(message)
