from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseModel):
    host: str = Field(alias="DB_HOST", default="localhost")
    port: int = Field(alias="DB_PORT", default=5432)
    user: str = Field(alias="DB_USER", default="dnd_guide")
    password: str = Field(alias="DB_PASSWORD", default="dnd_guide")
    database_name: str = Field(alias="DB_DATABASE", default="dnd_guide")

    def url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database_name}"


class Settings(BaseSettings):
    db_settings: DatabaseSettings = DatabaseSettings()


settings = Settings()
