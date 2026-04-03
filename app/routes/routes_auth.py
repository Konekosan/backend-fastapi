from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, joinedload
from app.database.database import get_db
from app.models.usager import Usager, Role
from app.schemas.usager import UsagerCreate, UsagerOut, LoginRequest, TokenResponse, MeResponse
from app.auth.auth import hash_password, verify_password, create_access_token
from app.auth.dependencies import get_current_user, get_user_permissions


auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/register", response_model=UsagerOut, status_code=201)
def register(payload: UsagerCreate, db: Session = Depends(get_db)):
    existing_user = db.query(Usager).filter(Usager.email == payload.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email déjà utilisé"
        )

    role_user = db.query(Role).filter(Role.nom == "Utilisateur").first()
    if not role_user:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Le rôle 'user' n'existe pas en base"
        )

    new_user = Usager(
        nom=payload.nom,
        email=payload.email,
        sexe=payload.sexe,
        identifiant=payload.identifiant,
        adresse=payload.adresse,
        date_naissance=payload.date_naissance,
        hashed_password=hash_password(payload.hashed_password),
        is_active=True
    )

    new_user.roles.append(role_user)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@auth_router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = (
        db.query(Usager)
        .options(joinedload(Usager.roles))
        .filter(Usager.email == payload.email)
        .first()
    )

    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou mot de passe invalide"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Compte désactivé"
        )

    access_token = create_access_token(data={"sub": str(user.id)})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@auth_router.get("/me", response_model=MeResponse)
def me(current_user: Usager = Depends(get_current_user)):
    roles = [role.nom for role in current_user.roles]
    permissions = sorted(list(get_user_permissions(current_user)))

    return {
        "id": current_user.id,
        "nom": current_user.nom,
        "email": current_user.email,
        "roles": roles,
        "permissions": permissions
    }