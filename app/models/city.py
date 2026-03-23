from pydantic import BaseModel

class City:
    name: str
    lat: int
    long: int

class CitiesResponse:
    name: str
    temperature: str
    vent: str