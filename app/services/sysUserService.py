from sqlalchemy.orm import Session
from app.dto.SysUserDTO import SysUserDTO

class SysUserService:
    def __init__(self, db: Session):
        self.db = db

    def create_sys_user(self, user_dto: SysUserDTO):
        print(f"Creating system user: {user_dto.username}")
        pass