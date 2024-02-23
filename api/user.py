import os
import tempfile
from typing import List

from fastapi import APIRouter, Depends, UploadFile

from managers.user import UserManager
from services.files import write_data_from_file
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


@router.post("/import-from-csv")
async def import_from_csv(file: UploadFile):
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, file.filename)
        with open(file_path, "wb") as temp_file:
            temp_file.write(await file.read())

        await write_data_from_file(file_path)
