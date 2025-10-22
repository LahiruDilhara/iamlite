from pathlib import Path
from dotenv import load_dotenv
from app.log import logger
import os

load_dotenv()

# Application Configuration
APP_TITLE:str = "IAMLite"

# Postgresql Database Configuration
POSTGRES_DB_HOST:str = None
POSTGRES_DB_PORT:int = None
POSTGRES_DB_NAME:str = None
POSTGRES_DB_USER:str = None
POSTGRES_DB_PASSWORD:str = None

def init_config()->None:
    global POSTGRES_DB_HOST, POSTGRES_DB_PORT, POSTGRES_DB_NAME, POSTGRES_DB_USER, POSTGRES_DB_PASSWORD, APP_TITLE
    POSTGRES_DB_HOST = os.getenv("POSTGRES_DB_HOST",None)
    POSTGRES_DB_NAME = os.getenv("POSTGRES_DB_NAME",None)
    POSTGRES_DB_USER = os.getenv("POSTGRES_DB_USER",None)
    POSTGRES_DB_PASSWORD = os.getenv("POSTGRES_DB_PASSWORD",None)
    postgressPortStr = os.getenv("POSTGRES_DB_PORT",None)
    print(postgressPortStr)
    try:
        POSTGRES_DB_PORT = int(postgressPortStr) if postgressPortStr is not None else None
    except ValueError:
        logger.error("POSTGRES_DB_PORT must be an integer.")
        POSTGRES_DB_PORT = 0
    
    APP_TITLE = os.getenv("APP_TITLE", APP_TITLE)
    if POSTGRES_DB_HOST == None:
        logger.warning("POSTGRES_DB_HOST is not set in environment variables.")
    if POSTGRES_DB_PORT == None:
        logger.warning("POSTGRES_DB_PORT is not set in environment variables.")
    if POSTGRES_DB_NAME == None:
        logger.warning("POSTGRES_DB_NAME is not set in environment variables.")
    if POSTGRES_DB_USER == None:
        logger.warning("POSTGRES_DB_USER is not set in environment variables.")
    if POSTGRES_DB_PASSWORD == None:
        logger.warning("POSTGRES_DB_PASSWORD is not set in environment variables.")
    