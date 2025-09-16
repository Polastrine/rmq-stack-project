from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_VERSION: str
    API_HOST: str
    API_PORT: int
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int
    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str
    RABBITMQ_QUEUE: str
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()