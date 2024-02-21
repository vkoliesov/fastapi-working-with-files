from models import Category, Catalog
from db import database

categories = Category.metadata.tables.get("category")
catalogs = Catalog.metadat.tables.get("catalog")


class CategoryManager:
    """Base Category Manager."""

    @staticmethod
    async def get_category_by_name(category_name: str):
        """Get category by name method."""
        return await database.fetch_one(
            categories.select().where(categories.c.category == category_name)
        )

    @staticmethod
    async def get_category_by_id(id: int):
        """Get category by id method."""
        return await database.fetch_one(
            categories.select().where(categories.c.id == id)
        )

    @staticmethod
    async def get_or_create_category(category_name: str):
        """Get or create category method."""
        category = await CategoryManager.get_category_by_name(category_name)

        if not category:
            id_ = await database.execute(
                categories.insert().values({
                    "category": category_name
                })
            )
            return await CategoryManager.get_category_by_id(id_)
        return category
