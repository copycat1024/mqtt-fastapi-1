import paho.mqtt.client as mqtt
import json
import random
import time
from util.log import create_logger

if __name__ == "__main__":
    logger = create_logger("mqtt")
    client = mqtt.Client()
    client.connect("mosquitto")

    while True:
        connector = random.randint(0, 3)
        logger.info(f"Publish event on connector {connector}")
        data = {
            "session_id": 1,
            "duration": random.randint(55, 65),
            "energy_delivered": random.randint(0, 100),
            "session_cost": random.randint(0, 100),
        }
        client.publish(f"charger/1/connector/{connector}/session/1", json.dumps(data))
        time.sleep(10)
