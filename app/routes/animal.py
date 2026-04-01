from fastapi import APIRouter

router = APIRouter()

class AnimalAPI():
    def __init__(self, router):
        self.router = router
        self.register_routes()
    
    def register_routes(self):
        self.router.get('')(self)

