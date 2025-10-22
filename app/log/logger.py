from loguru import logger
import os
import sys

os.makedirs("logs", exist_ok=True)

logger.remove()

# Console handler: Only info and higher level logs will be shown in the console
logger.add(sys.stderr, format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="INFO")

# Every debug and higher level logs will be saved to a file with rotation
logger.add("logs/iamlight.log", rotation="10 MB", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="DEBUG")

def get_logger():
    return logger