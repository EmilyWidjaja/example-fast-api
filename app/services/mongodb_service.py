from app.core.ml_model import MLModel
import sys
import json
import pymongo
from bson.objectid import ObjectId
from bson import json_util
from loguru import logger

from app.core.settings import GLOBAL_CONFIG_OBJ
from app.core.ml_model import MLModel


class MongoDBService:
    """
    MongoDB database query methos
    """

    def __init__(self):
        super().__init__()
        logger.info("Initialise MongoDBService")

        self.client = None
        self.db = None
        self.connect()

    def connect(self):
        """
        Connect to MongoDB
        """
        logger.info("Connect to MongoDB")

        try:
            host = GLOBAL_CONFIG_OBJ["mongodb"]["url"]
            db = GLOBAL_CONFIG_OBJ["mongodb"]["db"]

            self.client = pymongo.MongoClient(host, 27017)
            self.db = self.client[db]

            logger.info(f"Connected to MongoDB host = {host}, db = {db}")

        except Exception as e:
            logger.error(f"MongoDB connection error: {e}")
            sys.exit(1)

    def get_models(self):
        coll_name = GLOBAL_CONFIG_OBJ["mongodb"]["collection"]["models"]
        coll = self.db[coll_name]
        result = []

        try:
            cursor = coll.find({})
            for doc in cursor:
                result.append(json.dumps(doc, default=json_util.default))

        except Exception as e:
            logger.error(f"error = {e}")

        return result

    def save_model(self, ml_model: MLModel):
        """
        Step 1: Find a model with name and version
        Step 2: If not found, save a new model & its confusion matrix
        """
        coll_name = GLOBAL_CONFIG_OBJ["mongodb"]["collection"]["models"]
        coll = self.db[coll_name]
        result = None

        try:
            doc = coll.find_one({"name": ml_model.name, "version": ml_model.version})
            if doc is not None:
                result = {
                    "response": f"model: {ml_model.name}, version: {ml_model.version} exists, id: {str(doc['_id'])}"
                }
                logger.info(f"{result}")

            else:
                doc = coll.insert_one(ml_model.dict())
                result = {
                    "response": f"created a new model & its confusion matrix, id: {doc.inserted_id}"
                }
                logger.info(f"{result}")

        except Exception as e:
            logger.error(f"error = {e}")

        return result

    def get_active_model_of_cls(self, cls: str):
        """
        Find active models by class
        """
        coll_name = GLOBAL_CONFIG_OBJ["mongodb"]["collection"]["models"]
        coll = self.db[coll_name]
        result = []

        try:
            cursor = coll.find({"cls": cls, "active": True})
            for doc in cursor:
                result.append(json.dumps(doc, default=json_util.default))

        except Exception as e:
            logger.error(f"error = {e}")

        return result
