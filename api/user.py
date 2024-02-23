from typing import List

from fastapi import APIRouter, Depends

from managers.user import UserManager
from schemas.request.user import UserFilter
from schemas.response.user import UserOut

router = APIRouter(
    tags=["User"],
    prefix="/users"
)


@router.get("/", response_model=List[UserOut])
async def get_all_users(filters: UserFilter = Depends()):
    """Get all users endpoind."""
    results = await UserManager.get_users(filters.dict())
    return results or []
