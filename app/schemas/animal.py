from pydantic import BaseModel

class Animal(BaseModel):
    nom: str
    age: str
    espece: str

class UsagerResponse(BaseModel):
    id: int
    nom: str
    email: str

    class Config:
        from_attributes = True