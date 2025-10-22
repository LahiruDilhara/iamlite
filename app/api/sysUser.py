from fastapi import APIRouter,Depends
from app.dto.SysUserDTO import SysUserDTO
from app.database import Database
from sqlalchemy.orm import Session
from app.services.sysUserService import SysUserService

database = Database()
sysUserService = SysUserService(database.getSession())

router = APIRouter(prefix="/sysUser", tags=["sysUser"])

@router.post("/register")
async def create_initial_sys_user(payload: SysUserDTO, db:Session = Depends(database.getSession)):
    sysUserService.create_sys_user(payload)
    pass