# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

from fastapi.exceptions import RequestValidationError
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from app.api.sysUser import router as sys_user_router
from app.config import Configuration
from app.database import Database
from app.log.logger import logger
from app.exceptionHandler import register_exception_handlers


# Load configurations
Configuration()

# Initialize the database
Database()

app = FastAPI(title=Configuration().get_app_config().APP_TITLE)
app.include_router(sys_user_router)

# Register exception handlers
register_exception_handlers(app=app)