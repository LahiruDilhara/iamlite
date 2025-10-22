from app.db.sqlite_session import engine,SessionLocal,BaseModel
from app.models.iam_config import IAMConfig
from app.models.iam_admin import IAMAdmin
from app.log.logger import logger
from app.config import SQLITE_DB_PATH
import os

def is_table_empty(table_class) -> bool:
    with SessionLocal() as session:
        count = session.query(table_class).count()
        return count == 0
    
def initialize_database():
    if not os.path.exists(SQLITE_DB_PATH):
        logger.info("SQLite database not found. Creating new database.")
        BaseModel.metadata.create_all(bind=engine)
        logger.info("Database and tables created successfully.")
    
    if is_table_empty(IAMConfig):
        with SessionLocal() as session:
            logger.info("IAMConfig table is empty. Adding default configuration.")
            defaultConfig = IAMConfig.get_default_config()
            session.add(defaultConfig)
            session.commit()
            logger.info("Default configuration added to IAMConfig table.")


def is_admin_exists() -> bool:
    with SessionLocal() as session:
        count = session.query(IAMAdmin).count()
        return count > 0