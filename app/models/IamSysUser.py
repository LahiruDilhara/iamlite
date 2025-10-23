from app.models.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, Text

class IAMSysUser(BaseModel):
    __tablename__ = "iam_sys_users"

    id = Column(Integer, primary_key=True,autoincrement=True,index=True)
    username = Column(String(150), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)