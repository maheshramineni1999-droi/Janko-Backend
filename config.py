from pydantic_settings import BaseSettings
from urllib.parse import quote_plus  # <--- Import this


class Settings(BaseSettings):
    PROJECT_NAME: str = "Janko API"
    VERSION: str = "1.0.0"

    # 1. Define your raw credentials here
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "Mahesh@882"  # Put the password with the @ symbol here
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_NAME: str = "janko_db"

    # 2. Automatically construct the Safe URL
    @property
    def DATABASE_URL(self) -> str:
        # quote_plus fixes the @ symbol issue automatically
        return f"postgresql://{self.DB_USER}:{quote_plus(self.DB_PASSWORD)}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
