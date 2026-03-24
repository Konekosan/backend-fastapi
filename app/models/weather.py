from pydantic import BaseModel
from typing import List

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
    weathercode: int

class HourlyUnit(BaseModel):
    time: str
    temperature_2m: str
    weathercode: str

class Hourly(BaseModel):
    time: List[str]
    temperature_2m: List[float]
    weathercode: List[int]

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