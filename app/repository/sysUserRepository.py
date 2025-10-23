from app.core.Singleton import Singleton
from app.models.IamSysUser import IAMSysUser
from sqlalchemy.orm import Session

class SysUserRepository(Singleton):

    def create_user(self, session:Session, sys_user: IAMSysUser) -> None:
        try:
            session.add(sys_user)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
    
    def get_sysUser_count(self, session:Session) -> int:
        return session.query(IAMSysUser).count()