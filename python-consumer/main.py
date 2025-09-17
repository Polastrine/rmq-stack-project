from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from app import (
    eletroniccomponents_controller
)

from app.core.config import settings
from app.core.config.receive import RabbitMQClient

rabbitmq_client = RabbitMQClient()
rabbitmq_client.connect()
rabbitmq_client.consume_messages()

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    docs_url=settings.PROJECT_DOCS_URL,  
    redoc_url=settings.PROJECT_REDOC_URL,  
    openapi_url=settings.PROJECT_OPENAPI_URL
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(eletroniccomponents_controller, prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=False
    )