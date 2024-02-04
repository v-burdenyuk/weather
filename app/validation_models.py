import re
from dataclasses import Field

from pydantic import BaseModel, constr, ConstrainedStr


class OpenWeatherMapResponseMain(BaseModel):
    temp: float


class OpenWeatherMapResponseModel(BaseModel):
    main: OpenWeatherMapResponseMain


class Regex(ConstrainedStr):
    regex = re.compile("^\d{4}-\d{2}-\d{2}$")


class Request(BaseModel):
    day: Regex
    x_token: str
