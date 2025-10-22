from sqlalchemy import create_engine,Engine
from sqlalchemy.orm import sessionmaker, Session
from app.config import Configuration
from app.log.logger import logger
from typing import Generator
from app.models.BaseModel import BaseModel

# import models to register them with BaseModel
from app.models import IamConfig,IamSysUser


class Database():
    _instance = None
    _session: sessionmaker[Session] = None
    _engine: Engine = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        logger.debug("Database instance created.")
        config = Configuration().get_db_config()
        dbUrl = f"postgresql+psycopg2://{config.POSTGRES_DB_USER}:{config.POSTGRES_DB_PASSWORD}@{config.POSTGRES_DB_HOST}:{config.POSTGRES_DB_PORT}/{config.POSTGRES_DB_NAME}"

        if self._engine is None:
            self._engine = create_engine(dbUrl)

        if self._session is None:
            self._session = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        
        logger.info("Database initialized successfully.")

        self.init_tables()
    
    def init_tables(self):
        BaseModel.metadata.create_all(bind=self._engine)
        logger.info("Database tables created successfully.")
    
    def getSession(self)->Generator[Session,None,None]:
        db = self._session()
        try:
            yield db
        finally:
            db.close()
    
    def getEngine(self)->Engine:
        return self._engine