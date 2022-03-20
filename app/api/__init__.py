from fastapi import APIRouter

from . import create, retrieve

api_router = APIRouter()
api_router.include_router(create.router)
api_router.include_router(retrieve.router)
