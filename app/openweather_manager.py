import json
import os

from pydantic import parse_obj_as

from app.models import TemperatureHistory
from app.validation_models import OpenWeatherMapResponseModel
from app.open_weather_client import OpenWeatherMapApiClient


class OpenWeatherManager:
    client = OpenWeatherMapApiClient()

    def _get_weather_now(self) -> OpenWeatherMapResponseModel:
        current_weather_response = self.client.get_current_weather()

        open_weather_map_response_model = parse_obj_as(
            OpenWeatherMapResponseModel,
            json.loads(current_weather_response.text)
        )
        return open_weather_map_response_model

    def _get_temperature_now(self) -> float:
        current_weather = self._get_weather_now()
        return current_weather.main.temp

    async def store_current_temperature(self) -> None:
        temperature_now = self._get_temperature_now()
        await TemperatureHistory(city=os.environ.get("CITY"), temperature=temperature_now).save()
