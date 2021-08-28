from app.api.routing.cars import router as cars_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(cars_router, prefix="/cars", tags=["cars"])
