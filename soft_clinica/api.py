from ninja import NinjaAPI

from pacientes.api import router as pacientes_router

api = NinjaAPI()

api.add_router('/', pacientes_router)
