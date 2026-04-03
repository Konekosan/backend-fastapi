from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from models.usager import Usager
from schemas.usager import UsagerOut
from auth.dependencies import get_current_user, require_permission

router = APIRouter(prefix="/usagers", tags=["usagers"])


@router.get("/protected")
def protected_route(current_user: Usager = Depends(get_current_user)):
    return {
        "message": f"Bonjour {current_user.nom}, tu es authentifié"
    }


@router.get("/", response_model=list[UsagerOut])
def get_all_usagers(
    db: Session = Depends(get_db),
    current_user: Usager = Depends(require_permission("read_usager"))
):
    return db.query(Usager).all()


@router.delete("/{usager_id}")
def delete_usager(
    usager_id: int,
    db: Session = Depends(get_db),
    current_user: Usager = Depends(require_permission("delete_usager"))
):
    usager = db.query(Usager).filter(Usager.id == usager_id).first()
    if not usager:
        return {"message": "Usager introuvable"}

    db.delete(usager)
    db.commit()

    return {"message": f"Usager {usager_id} supprimé"}