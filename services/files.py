import aiofiles
from datetime import datetime

from constants import DATA_FILE_FOLDER_PATH
from managers.user import UserManager


async def write_data_from_file(file_path=None):
    """Write data from file to database."""
    if file_path is None:
        file_path = DATA_FILE_FOLDER_PATH
    async with aiofiles.open(file_path, "r") as file:
        await file.readline()
        async for line in file:
            category, first_name, last_name, email, gender, birth_date = line.strip().split(",")

            await UserManager.get_or_create_user(
                {
                    "category": category,
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "gender": gender.upper(),
                    "birth_date": datetime.strptime(
                        birth_date, "%Y-%m-%d"
                    ).date()
                }
            )
