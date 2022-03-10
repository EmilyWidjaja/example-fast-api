from fastapi import APIRouter, Depends

from app.controllers.example_controller import example_router

router = APIRouter()

router.include_router(
    example_router,
    prefix="/api/example",
)
