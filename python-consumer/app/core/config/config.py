from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    PROJECT_NAME: str
    PROJECT_VERSION: str
    PROJECT_DESCRIPTION: str
    PROJECT_DOCS_URL: str = "/docs"  
    PROJECT_REDOC_URL: str = "/redoc"  
    PROJECT_OPENAPI_URL: str = "/openapi.json"  
    API_HOST: str
    API_PORT: int
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int
    RABBITMQ_QUEUE: str
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()