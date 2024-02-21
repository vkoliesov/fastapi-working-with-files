from models import User
from db import database

users = User.metadat.tables.get("user")


class UseryManager:
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
        user = await UseryManager.get_user_by_email(user_email)

        if not user:
            id_ = await database.execute(
                users.insert().values(**user_data)
            )
            return await UseryManager.get_user_by_id(id_)
        return user
