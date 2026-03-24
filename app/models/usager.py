from pydantic import BaseModel
from datetime import datetime

class Usager(BaseModel):
    id: int
    nom: str
    prenom: str
    age: int
    date_naissance: datetime
