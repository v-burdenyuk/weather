from pydantic import BaseModel


class OpenWeatherMapResponseMain(BaseModel):
    temp: float


class OpenWeatherMapResponseModel(BaseModel):
    main: OpenWeatherMapResponseMain


class Request(BaseModel):
    day: str
    x_token: str
