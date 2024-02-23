from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, validator


class UserFilter(BaseModel):
    """Base user filters."""

    category: Optional[str] = Field(default=None, example="food")
    gender: Optional[str] = Field(default=None, example="male")
    birth_date_from: Optional[date] = Field(default=None, example="1996-03-07")
    birth_date_to: Optional[date] = Field(default=None, example="2024-02-22")
    age_from: Optional[int] = Field(default=None, example="18")
    age_to: Optional[int] = Field(default=None, example="27")
    limit: Optional[int] = Field(default=100, example="20")
    offset: Optional[int] = Field(default=0, example="20")

    @validator("age_from", "age_to")
    def validate_age(cls, v):
        """Age validation."""
        if v is not None and (v < 0 or v > 150):
            raise ValueError("Age must be between 0 and 150")
        return v

    @validator("birth_date_from", "birth_date_to")
    def validate_dates(cls, v, values, **kwargs):
        """Birth dates validation."""
        if "birth_date_from" in values and "birth_date_to" in values:
            if values["birth_date_from"] and values["birth_date_to"] and v:
                if values["birth_date_from"] > values["birth_date_to"]:
                    raise ValueError(
                        "birth_date_from must be earlier than birth_date_to"
                    )
        return v
