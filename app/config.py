# used to set database location
from pydantic import BaseSettings
from src.helpers import DATABASE_LOCATION


class Settings(BaseSettings):
    database: str = DATABASE_LOCATION


settings = Settings()
