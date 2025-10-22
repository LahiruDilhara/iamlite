from app.db.sqlite_session import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, Text
from app.config import SQLITE_CONFIG_TABLE_NAME

class IAMConfig(BaseModel):
    __tablename__ = SQLITE_CONFIG_TABLE_NAME

    id = Column(Integer, primary_key=True,autoincrement=True,index=True)
    config_name = Column(String(255), nullable=False, unique=True)
    value = Column(Text, nullable=False)
    description = Column(Text, nullable=True)

    def get_default_config():
        return IAMConfig(
            config_name="default_config",
            value="default_value",
            description="This is the default IAM configuration."
        )