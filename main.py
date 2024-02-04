import logging
import os
import sys

from fastapi import FastAPI, HTTPException
from fastapi_utils.tasks import repeat_every
from tortoise.contrib.fastapi import register_tortoise
from app.models import TemperatureHistory
from app.openweather_manager import OpenWeatherManager
from app.validation_models import Request

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

app = FastAPI()


@app.post("/hourly_temperature")
async def get_hourly_temperature(request: Request):
    if request.x_token != os.environ.get("X_TOKEN"):
        raise HTTPException(status_code=403, detail="Invalid X_TOKEN")
    return await TemperatureHistory.filter(datetime__startswith=request.day)  # TODO: aggregate by hour


@app.on_event("startup")
@repeat_every(seconds=60 * 60)  # hourly
async def get_weather() -> None:
    await OpenWeatherManager().store_current_temperature()


register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",  # TODO: migrate to something more permanent and productive
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
