from fastapi import APIRouter
from typing import List
from app.models.fruit import Fruit
from app.controller.fruit_controller import get_all_fruits, get_fruit_by_id, get_fruit_by_name
from fastapi import HTTPException

router = APIRouter()


@router.get('/', response_model=List[Fruit])
async def get_fruits():
    try:
        return await get_all_fruits()
    except Exception:
        raise HTTPException(status_code=500, detail='API Error')


@router.get('/{id}' , response_model=Fruit)
async def get_fruit(id: int):
    try:
        return await get_fruit_by_id(id)
    except Exception:
        raise HTTPException(status_code=500, detail='Erreur lors du fetch des donnes')


@router.get('/detail/{name}', response_model=Fruit)
async def get_fruit_api_by_name(name: str) -> Fruit:
    try:
        return await get_fruit_by_name(name)
    except Exception:
        raise HTTPException(status_code=500, detail='Erreur lors du fetch des donnes')