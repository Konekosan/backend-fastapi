from fastapi import APIRouter
from app.database.database import get_db
from app.models.usager import Usager
from app.schemas.usager import UsagerCreate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

router = APIRouter()

class UsagerAPI():
    def __init__(self, router: APIRouter):
        self.router = router
        self.register_routes()
    
    def register_routes(self):
        self.router.get('')(self.returnSimpleObject)
        self.router.get('/usagers')(self.get_usagers)
        self.router.post('/create')(self.create_usager)

    def returnSimpleObject(self):
        return { 'result' : '200' }

    def create_usager(self, usager: UsagerCreate, db: Session = Depends(get_db)):
        try:
            user = Usager(**usager.model_dump(exclude_unset=True))
            db.add(user)
            db.commit()
            db.refresh(user)
            return user
        except Exception as e:
            print(e)

    def get_usagers(self, db: Session = Depends(get_db)):
        try:
            usagers = db.query(Usager).all()
            return usagers
        except Exception as e:
            print(e)
            return []


UsagerAPI(router)