from fastapi import APIRouter

from api import user

api_router = APIRouter()
api_router.include_router(user.router)
