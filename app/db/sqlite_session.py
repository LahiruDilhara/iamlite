# from pathlib import Path
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from app.config import SQLITE_DB_PATH

# SQLITE_DATABASE_URL = f"sqlite:///{SQLITE_DB_PATH}"

# engine = create_engine(SQLITE_DATABASE_URL,connect_args={"check_same_thread": False})

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# BaseModel = declarative_base()

# def get_sqlite_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()