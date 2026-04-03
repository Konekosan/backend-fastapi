from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session, joinedload

from .auth import decode_access_token
from app.database.database import get_db
from app.models.usager import Usager, Role

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    token = credentials.credentials
    payload = decode_access_token(token)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalide ou expiré"
        )

    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalide"
        )

    user = (
        db.query(Usager)
        .options(
            joinedload(Usager.roles).joinedload(Role.permissions)
        )
        .filter(Usager.id == int(user_id))
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Utilisateur introuvable"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Utilisateur désactivé"
        )

    return user


def get_user_permissions(user: Usager) -> set[str]:
    permissions = set()
    for role in user.roles:
        for permission in role.permissions:
            permissions.add(permission.nom)
    return permissions


def require_permission(permission_name: str):
    def permission_checker(current_user: Usager = Depends(get_current_user)):
        permissions = get_user_permissions(current_user)
        if permission_name not in permissions:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Permission manquante: {permission_name}"
            )
        return current_user

    return permission_checker