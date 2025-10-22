from sqlalchemy import Column, Integer, String, Boolean, Text
from app.models.BaseModel import BaseModel

class IAMConfig(BaseModel):
    __tablename__ = "iam_configs"

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