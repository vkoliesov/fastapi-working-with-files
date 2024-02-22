from datetime import date
from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    first_name: int
    last_name: int
    email: int
    gender: str
    birth_date: date
