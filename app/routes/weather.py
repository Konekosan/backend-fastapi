from fastapi import APIRouter
from app.controller.weather_controller import fetchWeatherByCity
from fastapi import HTTPException

router = APIRouter()

@router.get('/')
async def get_weather():
    try:
        return await fetchWeatherByCity()
    except Exception:
        raise HTTPException(status_code=500, detail='API Error')
