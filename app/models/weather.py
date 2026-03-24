from pydantic import BaseModel
from typing import List
from enum import IntEnum


class WeatherCode(IntEnum):
    CLEAR = 0
    PARTLY_CLOUDY = 1
    UN_CAS_INCONNU = 2
    CLOUDY = 3
    FOG = 45
    DRIZZLE = 51
    RAIN = 61
    SNOW = 71
    THUNDERSTORM = 95    

class CurrentUnit(BaseModel):
    time: str
    interval: str
    temperature_2m: str
    wind_speed_10m: str
    weathercode: str

class Current(BaseModel):
    time: str
    interval: int
    temperature_2m: float
    wind_speed_10m: float
    weathercode: WeatherCode

class HourlyUnit(BaseModel):
    time: str
    temperature_2m: str
    weathercode: str

class Hourly(BaseModel):
    time: List[str]
    temperature_2m: List[float]
    weathercode: List[WeatherCode]

class Weather(BaseModel):
    latitude: float
    longitude: float
    generationtime_ms: float
    utc_offset_seconds: int
    timezone: str
    timezone_abbreviation: str
    elevation: int
    current_units: CurrentUnit
    current: Current
    hourly_units: HourlyUnit
    hourly: Hourly