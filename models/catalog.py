import sqlalchemy as sa

from db import Base
from models.base import BaseMixin


class Category(BaseMixin, Base):
    """Category model."""

    __tablename__ = "category"

    category = sa.Column(sa.String(15), nullable=False, unique=True)


class Catalog(BaseMixin, Base):
    """Catalog model."""

    __tablename__ = "catalog"
    __table_args__ = (
        sa.UniqueConstraint(
            "category_id",
            "user_id",
            name="category_user_uc"
        ),
    )

    category_id = sa.Column(sa.ForeignKey("category.id"), nullable=False)
    user_id = sa.Column(sa.ForeignKey("user.id"), nullable=False)

    
