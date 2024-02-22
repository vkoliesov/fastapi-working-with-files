from pydantic import BaseModel, Field

from schemas.response.user import UserOut


class CategoryOut(BaseModel):
    """Category output model."""

    id: int = Field(example=1)
    category: str = Field(example="food")


class CatalogOut(BaseModel):
    """Catalog output model."""

    id: int = Field(example=1)
    user: UserOut
    category: CategoryOut
