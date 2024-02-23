from datetime import date, timedelta

from constants import YEAR_DAYS
from models import User
from db import database

users = User.metadata.tables.get("user")


class UserManager:
    """Base User Manager."""

    @staticmethod
    async def get_user_by_email(email: str):
        """Get user by email method."""
        return await database.fetch_one(
            users.select().where(users.c.email == email)
        )

    @staticmethod
    async def get_user_by_id(id: int):
        """Get user by id method."""
        return await database.fetch_one(
            users.select().where(users.c.id == id)
        )

    @staticmethod
    async def get_or_create_user(user_data: dict):
        """Get or create user method."""
        user_email = user_data.get("email")
        user = await UserManager.get_user_by_email(user_email)

        if not user:
            id_ = await database.execute(
                users.insert().values(**user_data)
            )
            return await UserManager.get_user_by_id(id_)
        return user

    @staticmethod
    async def get_users(filters: dict):
        """Get users method."""
        query = users.select()

        if filters.get("category"):
            query = query.where(users.c.category == filters.get("category"))
        if filters.get("gender"):
            query = query.where(
                users.c.gender == filters.get("gender").upper()
            )
        if filters.get("birth_date_from") and filters.get("birth_date_to"):
            query = query.where(
                users.c.date_of_birth.between(
                    filters.get("birth_date_from"),
                    filters.get("birth_date_to")
                )
            )
        today = date.today()
        if filters.get("age_from"):
            date_from = today - timedelta(
                days=YEAR_DAYS * (filters.get("age_from") + 1)
            )
            query = query.where(users.c.date_of_birth <= date_from)

        if filters.get("age_to"):
            date_to = today - timedelta(
                days=YEAR_DAYS * filters.get("age_to")
            )
            query = query.where(users.c.date_of_birth >= date_to)
        if filters.get("limit"):
            query = query.limit(filters.get("limit"))
        return await database.fetch_all(query)
