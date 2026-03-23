import httpx
from typing import List
from app.models.fruit import Fruit
from app.models.city import City

URL = 'https://api.open-meteo.com/v1/forecast?latitude=$44.836151&longitude=$-0.580816&current=temperature_2m,wind_speed_10m,weathercode&hourly=temperature_2m,weathercode'

async def fetchWeatherByCity():
    async with httpx.AsyncClient() as client:
        response = await client.get(URL)
        response.raise_for_status()
        data = response.json()

    return data

async def fetchAllWeatherCities():
    async with httpx.AsyncClient() as client:
        print(client)
        response = await client.get('/')
        



city: List[City] = [
  { 'name': 'Paris', 'lat': 48.8566, 'lon': 2.3522 },
  { 'name': 'Lyon', 'lat': 45.7640, 'lon': 4.8357 },
  { 'name': 'Marseille', 'lat': 43.2965, 'lon': 5.3698 },
  { 'name': 'Toulouse', 'lat': 43.6047, 'lon': 1.4442 },
  { 'name': 'Nice', 'lat': 43.7102, 'lon': 7.2620 },
  { 'name': 'Nantes', 'lat': 47.2184, 'lon': -1.5536 },
  { 'name': 'Strasbourg', 'lat': 48.5734, 'lon': 7.7521 },
  { 'name': 'Bordeaux', 'lat': 44.836151, 'lon': -0.580816 },
]

