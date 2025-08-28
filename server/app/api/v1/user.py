from fastapi import APIRouter, Depends
from app.schemas.user import UserOut
from app.api.deps import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserOut)
async def read_current_user(current_user = Depends(get_current_user)):
    return current_user
