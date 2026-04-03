from pydantic import BaseModel
from datetime import datetime

# class UsagerCreate(BaseModel):
#     nom: str
#     email: str
#     sexe: str
#     adresse: str
#     date_naissance: datetime

# class UsagerResponse(BaseModel):
#     id: int
#     nom: str
#     email: str
#     sexe: str
#     adresse: str
#     date_naissance: datetime

#     class Config:
#         from_attributes = True

from datetime import date
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class PermissionOut(BaseModel):
    id: int
    nom: str

    class Config:
        from_attributes = True


class RoleOut(BaseModel):
    id: int
    nom: str
    permissions: List[PermissionOut] = []

    class Config:
        from_attributes = True


class UsagerCreate(BaseModel):
    nom: str
    email: EmailStr
    identifiant: str
    hashed_password: str
    sexe: Optional[str] = None
    adresse: Optional[str] = None
    date_naissance: Optional[date] = None



class UsagerOut(BaseModel):
    id: int
    nom: str
    email: EmailStr
    sexe: Optional[str] = None
    adresse: Optional[str] = None
    date_naissance: Optional[date] = None
    is_active: bool
    roles: List[RoleOut] = []

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class MeResponse(BaseModel):
    id: int
    nom: str
    email: EmailStr
    roles: List[str]
    permissions: List[str]