import aiofiles
from datetime import datetime

from constants import DATA_FILE_FOLDER_PATH
from managers.catalog import CategoryManager, CatalogManager
from managers.user import UseryManager


async def read_file(file_path):
    """Read data from file method."""
    async with aiofiles.open(file_path, "r") as file:
        await file.readline()
        async for line in file:
            yield line.strip().split(",")
        return


async def write_data_from_file():
    """Write data from file to database."""
    async for values in read_file(DATA_FILE_FOLDER_PATH):
        category_name = values.pop(0)
        first_name, last_name, email, gender, birth_date = values
        category = await CategoryManager\
            .get_or_create_category(category_name=category_name)

        user = await UseryManager.get_or_create_user(
            {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "gender": gender.upper(),
                "birth_date": datetime.strptime(birth_date, "%Y-%m-%d").date()
            }
        )
        await CatalogManager.get_or_create_catalog_item(
            user_id=user.id,
            category_id=category.id
        )
        return
