import json
from loguru import logger
from fastapi import APIRouter, Depends, Response, Query
from starlette.exceptions import HTTPException
from starlette.status import (
    HTTP_422_UNPROCESSABLE_ENTITY,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from app.utils.jwt_service import validate_user_token
from app.core.ml_model import MLModel
from app.services.mongodb_service import MongoDBService
from app.core.ml_model import MLModel


model_controller = APIRouter()


@model_controller.get("")
async def get_models(
    database_service: MongoDBService = Depends(MongoDBService),
):
    """
    Retrieve all models information
    """

    try:
        result = database_service.get_models()
        return Response(content=json.dumps(result), media_type="application/json")
    except Exception as e:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{e}",
        )


@model_controller.post("/model")
async def save_model(
    query: MLModel,
    database_service: MongoDBService = Depends(MongoDBService),
):
    """
    Save a model in the database
    """
    logger.info(f"Received ml model = {query}")

    try:
        result = database_service.save_model(query)
        return Response(content=json.dumps(result), media_type="application/json")
    except Exception as e:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{e}",
        )


@model_controller.get("/model")
async def get_active_model_of_cls(
    cls=Query(None),
    database_service: MongoDBService = Depends(MongoDBService),
):
    """
    Retrieve the active model of a class
    """
    logger.info(f"Received cls = {cls}")

    try:
        result = database_service.get_active_model_of_cls(cls)
        return Response(content=json.dumps(result), media_type="application/json")
    except Exception as e:
        raise HTTPException(
            status_code=HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"{e}",
        )
