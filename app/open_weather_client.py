import os

from requests import Response

from app.client import APIClient


class OpenWeatherMapApiClient(APIClient):
    api_base = "https://api.openweathermap.org/data/2.5/weather"

    def get_current_weather(self) -> Response:
        parameters = {
            "units": "metric",
            "q": os.environ.get("CITY"),
            "appid": os.environ.get("OPENWEATHERMAP_APIKEY")
        }
        return self.request(method="get", url=self.api_base, parameters=parameters)
