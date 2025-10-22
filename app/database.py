from sqlalchemy import create_engine,Engine
from sqlalchemy.orm import sessionmaker, declarative_base,Session
from app.config import POSTGRES_DB_HOST, POSTGRES_DB_PORT, POSTGRES_DB_NAME, POSTGRES_DB_USER, POSTGRES_DB_PASSWORD
from app.log.logger import logger

DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_DB_USER}:{POSTGRES_DB_PASSWORD}@{POSTGRES_DB_HOST}:{POSTGRES_DB_PORT}/{POSTGRES_DB_NAME}"

engine:Engine = None
SessionLocal:sessionmaker[Session] = None

def init_database():
    global engine, SessionLocal
    # try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    #     logger.info("Database initialized successfully.")
    # except Exception as e:
    #     logger.error(f"Error initializing database: {e}")
    