from pydantic import BaseSettings

class Settings(BaseSettings):
    env: str = "development"
    log_level: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
