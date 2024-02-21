import databases
import sqlalchemy
from decouple import config
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = f'postgresql://'\
                f'{config("POSTGRES_USER")}:'\
                f'{config("POSTGRES_PASSWORD")}@'\
                f'{config("POSTGRES_HOST")}:'\
                f'{config("POSTGRES_PORT")}/'\
                f'{config("POSTGRES_DB")}'

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

Base = declarative_base(metadata=metadata)
