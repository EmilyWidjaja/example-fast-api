import logging
import sys

from app.core.logging import InterceptHandler
from loguru import logger
from starlette.config import Config

config = Config(".env")

PROJECT_TITLE: str = config("PROJECT_TITLE", default="")
PROJECT_DESCRIPTION: str = config("PROJECT_DESCRIPTION", default="")
PROJECT_VERSION: str = config("PROJECT_VERSION", default="0.1")

DEBUG: bool = config("DEBUG", cast=bool, default=True)
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
logging.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
)
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
