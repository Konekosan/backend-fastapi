from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Animal(Base):

    __tablename__ = 'animaux'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nom = Column(String)
    age = Column(String, unique=True, index=True)
    espece = Column(String, unique=True, index=True)