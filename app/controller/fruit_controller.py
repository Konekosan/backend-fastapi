import httpx
from typing import List
from app.models.fruit import Fruit

URL = 'https://www.fruityvice.com/api/fruit/'


async def get_all_fruits() -> List[Fruit]:
    async with httpx.AsyncClient() as client:
        response = await client.get(URL + 'all')
        response.raise_for_status()
        data = response.json()

    return [Fruit(**fruit) for fruit in data]


async def get_fruit_by_id(id: int) -> Fruit:
    if id:
        async with httpx.AsyncClient() as client:
            response = await client.get(f'{URL}{id}')
            response.raise_for_status()
            data = response.json()
        return Fruit(**data)
    return None


async def get_fruit_by_name(name: str) -> Fruit:
    print(name)
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{URL}{name}')
        response.raise_for_status()
        data = response.json()
    return Fruit(**data)