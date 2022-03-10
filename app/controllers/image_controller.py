from loguru import logger
from fastapi import APIRouter, Depends, File, UploadFile

from app.utils.jwt_service import validate_user_token


image_controller = APIRouter()


@image_controller.post("/" )
async def save_model(file: UploadFile = File(...)):
    """
    Upload file and ...
    """
    logger.info(f"Received file name = {file.filename}")

    # TODO

    return {"file_name": file.filename}
