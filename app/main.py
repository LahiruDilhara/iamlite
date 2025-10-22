from fastapi import FastAPI
from app.db.db_initializer import initialize_database

# Initialize the database
initialize_database()


app = FastAPI(title="IAMLite")
