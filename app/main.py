from fastapi import FastAPI
from app.api.admin import router as admin_router
from app.config import init_config

# Initialize configurations
init_config()

# Initialize the database
# initialize_database()


app = FastAPI(title="IAMLite")
app.include_router(admin_router)