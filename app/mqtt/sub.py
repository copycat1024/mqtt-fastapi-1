import paho.mqtt.client as mqtt
from util.model import Message
from db.service import save_msg
from datetime import datetime
from tortoise import Tortoise, run_async
from util.log import create_logger
import re

DB_URL = "postgres://webster:pass123@db:5432/backend"
logger = create_logger("mqtt")


async def init_db():
    await Tortoise.init(db_url=DB_URL, modules={"models": ["db.model"]})
    await Tortoise.generate_schemas()


def on_message(client, userdata, msg):
    async def on_message_async():
        pattern = r"charger/(\d+)/connector/(\d+)/session/(\d+)"
        match = re.match(pattern, msg.topic)
        if match is not None:
            charger_id, connector_id, session_id = match.groups()
            message = Message(
                created_at=datetime.now(),
                charger_id=charger_id,
                connector_id=connector_id,
                session_id=session_id,
                payload=msg.payload,
            )
            logger.info(f"Subscriber received: {message}")
            await save_msg(message)

    run_async(on_message_async())


def on_connect(client, obj, flags, rc):
    topic = "charger/+/connector/+/session/+"
    client.subscribe(topic)
    logger.info(f"Connected, sub to {topic}")


if __name__ == "__main__":
    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_message = on_message
    run_async(init_db())

    client.connect("mosquitto")
    client.loop_forever()
