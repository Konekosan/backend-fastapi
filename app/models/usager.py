from pydantic import BaseModel
from datetime import datetime
from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Usager(Base):

    __tablename__ = 'usager'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nom = Column(String)
    email = Column(String, unique=True, index=True)
