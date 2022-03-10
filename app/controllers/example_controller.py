from loguru import logger
from fastapi import APIRouter, Depends, File, UploadFile


example_router = APIRouter()


@example_router.post("/")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload file and ...
    """
    logger.info(f"Received file name = {file.filename}")

    # TODO

    return {"file_name": file.filename}


@example_router.get("/")
async def example_get():
    """ """

    # TODO

    return {"response": "hello form get!"}
