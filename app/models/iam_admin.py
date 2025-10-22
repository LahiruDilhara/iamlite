from app.db.sqlite_session import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, Text
from app.config import SQLITE_ADMINS_TABLE_NAME

class IAMAdmin(BaseModel):
    __tablename__ = SQLITE_ADMINS_TABLE_NAME

    id = Column(Integer, primary_key=True,autoincrement=True,index=True)
    username = Column(String(150), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)