from fastapi import APIRouter
from app.database.database import get_db
from app.models.usager import Usager
from app.schemas.usager import UsagerCreate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.controller.usager_controller import UsagerController


router = APIRouter()
usager_controller = UsagerController()


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
            result = usager_controller.create_usager(usager, db)
            return result
        except Exception as e:
            print(e)

    def get_usagers(self, db: Session = Depends(get_db)):
        try:
            usagers = usager_controller.get_usagers(db)
            return usagers
        except Exception as e:
            print(e)
            return []


UsagerAPI(router)