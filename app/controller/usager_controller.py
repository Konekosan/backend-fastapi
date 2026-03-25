from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from app.database.database import get_db
from app.models.usager import Usager
from app.schemas.usager import UsagerCreate

class UsagerController():

    def get_usagers(self, db: Session = Depends(get_db)):
        usagers = db.query(Usager).all()
        return usagers

        
    def create_usager(self, usager: UsagerCreate, db: Session =  Depends(get_db)):
        user = Usager(**usager.model_dump(exclude_unset=True))
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
