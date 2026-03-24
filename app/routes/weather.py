from fastapi import APIRouter
from app.controller.weather_controller import fetchCITIES, getWeatherByCity
from fastapi import HTTPException

router = APIRouter()

class WeatherAPI():
    def __init__(self, router: APIRouter):
        self.router = router
        self.register_routes()

    def register_routes(self):
        self.router.get('')(self.get_CITIES)
        self.router.get('/{name}')(self.getWeatherByCityName)
    
    async def get_CITIES(self):
        try:
            return await fetchCITIES()
        except Exception:
            raise HTTPException(status_code=500, detail='API Error')
    
    async def getWeatherByCityName(self, name):
        try:
            #return {'city': name}
            return await getWeatherByCity(name)
        except Exception as e:
            print(e)

WeatherAPI(router)