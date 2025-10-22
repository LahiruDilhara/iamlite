from fastapi import FastAPI
from app.api.admin import router as admin_router
from app.config import init_config
from app.database import init_database

# Initialize configurations
init_config()

# Initialize the database
init_database()

# Initialize the database
# initialize_database()


app = FastAPI(title="IAMLite")
app.include_router(admin_router)