from typing import List, Optional

from fastapi import APIRouter

from managers.catalog import CatalogManager
from schemas.response.catalog import CatalogOut

router = APIRouter(
    tags=["Catalog"],
    prefix="/catalog"
)


@router.get("/", response_model=List[CatalogOut])
async def get_data(
    category: Optional[str] = None,
    gender: Optional[str] = None,
    date_of_birth: Optional[str] = None,
    age: Optional[int] = None,
    age_from: Optional[int] = None,
    age_to: Optional[int] = None,
):
    results = await CatalogManager.get_catalogs(
        category=category,
        gender=gender,
        date_of_birth=date_of_birth,
        age=age,
        age_from=age_from,
        age_to=age_to
    )
    return results or []
