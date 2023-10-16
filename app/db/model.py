from tortoise import fields, models


class Message(models.Model):
    created_at = fields.DatetimeField()
    charger_id = fields.IntField()
    connector_id = fields.IntField()
    session_id = fields.IntField()
    payload = fields.JSONField()
