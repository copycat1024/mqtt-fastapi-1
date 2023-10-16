import re
import os
import paho.mqtt.client as mqtt


from tortoise import Tortoise, run_async
from util.log import create_logger
from .session import SessionFilter


logger = create_logger("mqtt")

# a list of filter that process different MQTT messages of many topic
filters = [
    SessionFilter(),
]


async def init_db():
    await Tortoise.init(db_url=os.getenv("DB_URL"), modules={"models": ["db.model"]})
    await Tortoise.generate_schemas()


def on_connect(client, obj, flags, rc):
    # subscribe to any session of any charger
    topic = "charger/+/connector/+/session/+"
    client.subscribe(topic)
    logger.info(f"Connected and subscribed to {topic}")


def on_message(client, userdata, msg):
    # async function that will be run in sync method
    async def on_message_async():
        for filter in filters:
            await filter.process(msg)

    run_async(on_message_async())


if __name__ == "__main__":
    client = mqtt.Client()

    # set up event call back for client
    client.on_connect = on_connect
    client.on_message = on_message

    # init database schema
    run_async(init_db())

    # connect to broker and process messages
    client.connect("mosquitto")
    client.loop_forever()
