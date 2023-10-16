from datetime import datetime
from pydantic import BaseModel
from typing import Any


class Message(BaseModel):
    created_at: datetime
    charger_id: int
    connector_id: int
    session_id: int
    payload: Any

    def __str__(self):
        res = "Message {\n"
        res += f"  created_at: {self.created_at}\n"
        res += f"  charger_id: {self.charger_id}\n"
        res += f"  connector_id: {self.connector_id}\n"
        res += f"  session_id: {self.session_id}\n"
        res += f"  payload: {self.payload}\n"
        res += "}"

        return res
