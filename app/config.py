from pathlib import Path
from dotenv import load_dotenv
from app.log import logger
import os

load_dotenv()

# Application Configuration
APP_TITLE = "IAMLite"

# Postgresql Database Configuration
POSTGRES_DB_HOST = None
POSTGRES_DB_PORT = None
POSTGRES_DB_NAME = None
POSTGRES_DB_USER = None
POSTGRES_DB_PASSWORD = None
DATABASE_CONFIGURATIONS_READY = False

def init_config()->None:
    global POSTGRES_DB_HOST, POSTGRES_DB_PORT, POSTGRES_DB_NAME, POSTGRES_DB_USER, POSTGRES_DB_PASSWORD, APP_TITLE
    POSTGRES_DB_HOST = os.getenv("POSTGRES_DB_HOST")
    POSTGRES_DB_PORT = os.getenv("POSTGRES_DB_PORT")
    POSTGRES_DB_NAME = os.getenv("POSTGRES_DB_NAME")
    POSTGRES_DB_USER = os.getenv("POSTGRES_DB_USER")
    POSTGRES_DB_PASSWORD = os.getenv("POSTGRES_DB_PASSWORD")
    APP_TITLE = os.getenv("APP_TITLE", APP_TITLE)

    if not all([POSTGRES_DB_HOST, POSTGRES_DB_PORT, POSTGRES_DB_NAME, POSTGRES_DB_USER, POSTGRES_DB_PASSWORD]):
        logger.error("Database configuration is incomplete. Please set all required environment variables.")
        logger.error(f"POSTGRES_DB_HOST: {POSTGRES_DB_HOST}. POSTGRES_DB_PORT: {POSTGRES_DB_PORT}. POSTGRES_DB_NAME: {POSTGRES_DB_NAME}. POSTGRES_DB_USER: {POSTGRES_DB_USER}. POSTGRES_DB_PASSWORD: {'SET' if POSTGRES_DB_PASSWORD else 'NOT SET'}.")
        DATABASE_CONFIGURATIONS_READY = False
        return
    DATABASE_CONFIGURATIONS_READY = True