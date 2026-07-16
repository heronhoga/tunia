from fastapi import APIRouter
from services.auth_service import register 

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
    


