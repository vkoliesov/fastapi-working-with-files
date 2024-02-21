from fastapi import APIRouter

from api import catalog

api_router = APIRouter()
api_router.include_router(catalog.router)
