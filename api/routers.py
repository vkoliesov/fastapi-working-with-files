from fastapi import APIRouter

from api import read_file

api_router = APIRouter()
api_router.include_router(read_file.router)
