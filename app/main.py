from fastapi import FastAPI
from app.api.admin import router as admin_router
from app.config import Configuration
from app.database import Database
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load configurations
Configuration()

# Initialize the database
Database()

app = FastAPI(title=Configuration().get_app_config().APP_TITLE)
app.include_router(admin_router)