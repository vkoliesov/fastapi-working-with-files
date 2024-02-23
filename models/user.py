import sqlalchemy as sa

from db import Base
from models.base import BaseMixin
from models.enums import Gender


class User(BaseMixin, Base):
    """User model."""

    __tablename__ = "user"

    category = sa.Column(sa.String(50))
    first_name = sa.Column(sa.String(120))
    last_name = sa.Column(sa.String(120))
    email = sa.Column(sa.String(120), unique=True)
    gender = sa.Column(
        sa.Enum(Gender),
        nullable=False,
        server_default=Gender.FEMALE.name
    )
    birth_date = sa.Column(
        sa.Date, nullable=False,
        server_default=sa.func.now(),
    )
