from datetime import date
from typing import Optional

import sqlalchemy as sa

from models import Category, Catalog, User
from db import database
from services.age import calculate_dates_by_age

categories = Category.metadata.tables.get("category")
catalogs = Catalog.metadata.tables.get("catalog")
users = User.metadata.tables.get("user")


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


class CatalogManager:
    """Base Catalog Manager."""

    @staticmethod
    async def get_catalog_item(user_id: int, category_id: int):
        """Get catalog item by user and category name."""
        return await database.fetch_one(
            catalogs.select().where(
                catalogs.c.category_id == category_id,
                catalogs.c.user_id == user_id
            )
        )

    @staticmethod
    async def get_catalogs(
        category: Optional[str] = None,
        gender: Optional[str] = None,
        date_of_birth: Optional[date] = None,
        age: Optional[int] = None,
        age_from: Optional[int] = None,
        age_to: Optional[int] = None,
    ):
        """Get catalog item by user and category name."""
        join_condition = catalogs.c.category_id == categories.c.id
        join_condition &= catalogs.c.user_id == users.c.id
        joined_tables = sa.join(
            categories,
            sa.join(catalogs, users),
            onclause=join_condition
        )
        query = sa.select(
            [catalogs, users, categories]
        ).select_from(joined_tables)

        if category:
            query = query.where(categories.c.category == category)
        if gender:
            query = query.where(users.c.gender == gender.lower())
        if date_of_birth:
            query = query.where(users.c.date_of_birth == date_of_birth)
        if age:
            birth_dates_from, birth_dates_to = calculate_dates_by_age(age)
            query = query.where(
                users.c.date_of_birth >= birth_dates_from,
                users.c.date_of_birth <= birth_dates_to
            )
        elif age_from and age_to:
            birth_dates_from, _ = calculate_dates_by_age(age_from)
            _, birth_dates_to = calculate_dates_by_age(age_to)
            query = query.where(
                users.c.date_of_birth >= birth_dates_from,
                users.c.date_of_birth <= birth_dates_to
            )
        return await database.fetch_all(query)

    @staticmethod
    async def get_catalog_by_id(id: int):
        """Get category by id method."""
        return await database.fetch_one(
            catalogs.select().where(catalogs.c.id == id)
        )

    @staticmethod
    async def get_or_create_catalog_item(user_id: int, category_id: int):
        """Get or create catalog item method."""
        catalog_item = await CatalogManager\
            .get_catalog_item(user_id, category_id)

        if not catalog_item:
            id_ = await database.execute(
                catalogs.insert().values({
                    "user_id": user_id,
                    "category_id": category_id
                })
            )
            return await CatalogManager.get_catalog_by_id(id_)
        return catalog_item
