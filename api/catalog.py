from fastapi import APIRouter


router = APIRouter(
    tags=["Catalog"],
    prefix="/catalog"
)

@router.get("/")
async def get_data(
    category=None,
    gender=None,
    date_of_birth=None,
    age=None,
    age_from=None,
    age_to=None
):
    pass
