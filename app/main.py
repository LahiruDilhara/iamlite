# Load environment variables from .env file
from dotenv import load_dotenv
from fastapi.exceptions import RequestValidationError
load_dotenv()

from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from app.api.sysUser import router as sys_user_router
from app.config import Configuration
from app.database import Database
from app.log.logger import logger


# Load configurations
Configuration()

# Initialize the database
Database()

app = FastAPI(title=Configuration().get_app_config().APP_TITLE)
app.include_router(sys_user_router)

@app.exception_handler(404)
async def not_found_exception_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"error": "Not found"}
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Validation error: {exc.errors()}")
    error = "Validation error"

    if len(exc.errors()) >= 1:
        field = exc.errors()[0]["loc"][-1]
        msg = exc.errors()[0]["msg"]
        error = f"{field} {msg}"
    return JSONResponse(
        status_code=422,
        content={
            "error": error
        }
    )