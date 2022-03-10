import json
import os
from os import environ
from loguru import logger
from starlette.datastructures import CommaSeparatedStrings


DEFAULT_ROUTE_STR: str = ""

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

env = environ.get("ENV", "development")
logger.info(f"ENV = {env}")

if env == "production":
    GLOBAL_CONFIG_FILE = BASE_DIR + "/../../config/production.json"
else:
    GLOBAL_CONFIG_FILE = BASE_DIR + "/../../config/default.json"

RSA_PVT_KEY = BASE_DIR + "/../../config/keys/jwtRS256.key"
RSA_PUB_KEY = BASE_DIR + "/../../config/keys/jwtRS256.key.pub"

GLOBAL_CONFIG_OBJ = None
with open(GLOBAL_CONFIG_FILE) as config_file:
    GLOBAL_CONFIG_OBJ = json.load(config_file)


ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", "*"))
