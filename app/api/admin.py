from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["admin"])

@router.post("/initial")
async def create_initial_admin():
    print("Creating initial admin user...")
    pass