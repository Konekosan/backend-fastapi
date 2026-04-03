from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import fruit
from app.routes import weather
from app.routes import programmation
from app.routes import usager
from app.routes.routes_auth import auth_router

app = FastAPI()

origins = [
    'http://localhost:4200',
    'http://localhost',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]    
)

app.include_router(fruit.router, prefix='/fruits', tags=['fruits'])
app.include_router(weather.router, prefix='/weather', tags=['weather'])
app.include_router(programmation.router, prefix='/programmation', tags=['programmation'])
app.include_router(usager.router, prefix='/usager', tags=['usager'])
app.include_router(auth_router)