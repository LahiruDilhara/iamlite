from fastapi import FastAPI
from app.db.db_initializer import initialize_database
from app.api.admin import router as admin_router

# Initialize the database
initialize_database()


app = FastAPI(title="IAMLite")
app.include_router(admin_router)