from datetime import date
from pydantic import BaseModel, Field


class UserOut(BaseModel):
    """User output model."""

    id: int = Field(example=27)
    first_name: str = Field(example="Vladyslav")
    last_name: str = Field(example="Koliesov")
    email: str = Field(example="kolesov0703@gmail.com")
    gender: str = Field(example="male")
    birth_date: date = Field(example="1996-03-07")
