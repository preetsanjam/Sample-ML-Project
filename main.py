from src.logging import logger
from src.exception.exception import ProjectException
import sys

#print(logger.logging.info("Hello test log"))

try:
    print(1/0)
except Exception as e:
    raise ProjectException(e, sys)