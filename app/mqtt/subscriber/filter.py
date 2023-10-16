from abc import ABC
import re


class Filter(ABC):
    """
    Filter class that selective process MQTT message if its topic match
    the pattern
    """
    pattern: str = r".*?"

    def __init__(self):
        # compile the pattern
        self.re = re.compile(self.pattern)

    async def process(self, msg: any):
        """
        Process a message if its topic match the pattern
        """
        match = self.re.match(msg.topic)
        if match is not None:
            await self.handle(msg.payload, *match.groups())

    async def handle(self, payload, *args):
        """
        Handle a message whose topic match the pattern,
        should be implemented by derived class
        """
