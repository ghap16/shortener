from pydantic import BaseSettings


class Settings(BaseSettings):
    database_uri: str = "sqlite:///db.sqlite3"
    openapi_prefix: str = ""


settings = Settings()
