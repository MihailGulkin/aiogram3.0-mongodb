from dotenv import load_dotenv
from pydantic import BaseSettings, SecretStr

load_dotenv()


class Settings(BaseSettings):
    BOT_TOKEN: SecretStr
    MONGO_DB_URL: SecretStr

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


def get_settings() -> Settings:
    return Settings()
