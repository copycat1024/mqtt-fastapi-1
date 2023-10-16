import os
import logging
import logging.config
import json


def create_logger(name: str) -> logging.Logger:
    json_file = f"./log.{name}.json"
    if os.path.exists(json_file):
        with open(json_file, "rt") as f:
            config = json.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.INFO)

    return logging.getLogger(name)
