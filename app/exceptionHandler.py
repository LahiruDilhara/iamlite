from fastapi.responses import JSONResponse
from app.log.logger import logger
from fastapi import Request,FastAPI
from fastapi.exceptions import RequestValidationError
from app.core.exceptions import *

async def not_found_exception_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"error": "Not found"}
    )

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

async def service_validation_exception_handler(request: Request, exc: ValidationException):
    logger.error(f"Service validation error: {str(exc)}")
    return JSONResponse(
        status_code=400,
        content={"error": str(exc)}
    )

async def generic_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )


def register_exception_handlers(app:FastAPI):
    app.add_exception_handler(404, not_found_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(ValidationException, service_validation_exception_handler)
    app.add_exception_handler(Exception, generic_exception_handler)