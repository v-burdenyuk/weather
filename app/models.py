import datetime

from tortoise.models import Model
from tortoise import fields


class TemperatureHistory(Model):
    city = fields.CharField(max_length=255)
    datetime = fields.DatetimeField(default=datetime.datetime.now())
    temperature = fields.FloatField()

    def __str__(self):
        return f"{self.city}_{self.datetime}"
