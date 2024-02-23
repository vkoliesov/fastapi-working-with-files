import aiofiles
from datetime import datetime

from constants import DATA_FILE_FOLDER_PATH
from managers.user import UserManager


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
        category, first_name, last_name, email, gender, birth_date = values

        return await UserManager.get_or_create_user(
            {
                "category": category,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "gender": gender.upper(),
                "birth_date": datetime.strptime(birth_date, "%Y-%m-%d").date()
            }
        )
