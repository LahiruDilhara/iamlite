from sqlalchemy.orm import Session
from app.dto.SysUserDTO import SysUserDTO
from app.repository.sysUserRepository import SysUserRepository
from app.core.Singleton import Singleton
from app.models.IamSysUser import IAMSysUser
from app.util.passwordUtil import hash_password
from app.core.exceptions import ValidationException

repo = SysUserRepository()

class SysUserService(Singleton):

    def create_sys_user(self, db:Session, user_dto: SysUserDTO):
        current_user_count = repo.get_sysUser_count(db)
        if current_user_count > 0:
            raise ValidationException("System user already exists.")
        
        hashed_pw = hash_password(user_dto.password)
        sysUser = IAMSysUser(
            username=user_dto.username,
            email=user_dto.email,
            hashed_password=hashed_pw
        )
        repo.create_user(db, sysUser)