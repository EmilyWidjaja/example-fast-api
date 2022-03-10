from fastapi import APIRouter, Depends

from app.controllers.token_controller import token_controller
from app.controllers.model_controller import model_controller
from app.controllers.image_controller import image_controller
from app.utils.jwt_service import validate_user_token


router = APIRouter()

router.include_router(token_controller, prefix="/token")
router.include_router(
    image_controller,
    prefix="/api/image",
    dependencies=[Depends(validate_user_token)],
)
router.include_router(
    model_controller,
    prefix="/api/models",
    dependencies=[Depends(validate_user_token)],
)
