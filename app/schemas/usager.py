from pydantic import BaseModel

class UsagerCreate(BaseModel):
    nom: str
    email: str

class UsagerResponse(BaseModel):
    id: int
    nom: str
    email: str

    class Config:
        from_attributes = True