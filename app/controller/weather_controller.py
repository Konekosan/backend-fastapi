import httpx
from typing import List
from app.models.fruit import Fruit
from app.models.city import City
from app.models.weather import Weather
from app.models.city import CITIES
from fastapi import HTTPException

async def fetchCITIES():
    return CITIES

async def getWeatherByCity(name: str):
    if (name == None or name == ''):
        raise HTTPException(status_code=404, detail='Nom de Ville Inexistant')
    
    selected_city = next((city for city in CITIES if city.name.lower() == name.lower()), None)

    if (selected_city == None or selected_city == ''):
        raise HTTPException(status_code=405, detail='Ville non trouvée dans le référentiel')
    
    URL = f'https://api.open-meteo.com/v1/forecast?latitude={selected_city.lat}&longitude={selected_city.long}&current=temperature_2m,wind_speed_10m,weathercode&hourly=temperature_2m,weathercode'
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(URL)
            response.raise_for_status()
            data = response.json()
            weather = Weather(**data)
        return {'result': weather}

    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
