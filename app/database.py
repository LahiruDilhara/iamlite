from sqlalchemy import create_engine,Engine
from sqlalchemy.orm import sessionmaker, declarative_base,Session
from app.config import Configuration
from app.log.logger import logger

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
    
    def getSession(self)->Session:
        db = self._session()
        try:
            yield db
        finally:
            db.close()
    
    def getEngine(self)->Engine:
        return self._engine