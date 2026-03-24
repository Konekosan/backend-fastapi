from pydantic import BaseModel
from typing import List

class City(BaseModel):
    name: str
    lat: float
    long: float

class CitiesResponse:
    name: str
    temperature: str
    vent: str


CITIES: List[City] = [
    City(name='Paris', lat=48.8566, long=2.3522),
    City(name= 'Paris', lat= 48.8566, long= 2.3522 ),
    City(name= 'Lyon', lat= 45.7640, long= 4.8357 ),
    City(name= 'Marseille', lat= 43.2965, long= 5.3698 ),
    City(name= 'Toulouse', lat= 43.6047, long= 1.4442 ),
    City(name= 'Nice', lat= 43.7102, long= 7.2620 ),
    City(name= 'Nantes', lat= 47.2184, long= -1.5536 ),
    City(name= 'Strasbourg', lat= 48.5734, long= 7.7521 ),
    City(name= 'Bordeaux', lat= 44.836151, long= -0.580816 ),
]
