from fastapi import FastAPI
import uvicorn
import logging
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from fastapi.openapi.utils import get_openapi
from fastapi.staticfiles import StaticFiles

from app import (
    eletroniccomponents_controller
)
from app.core.config import settings
from app.core.consumer import RabbitMQConsumer


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

@app.on_event("startup")
async def startup_event():
    """Executado quando a aplicação é iniciada"""
    # Inicia o consumidor de RabbitMQ em uma thread separada
    RabbitMQConsumer.start_consumer()

@app.on_event("shutdown")
async def shutdown_event():
    """Executado quando a aplicação é encerrada"""
    RabbitMQConsumer.stop_consumer()

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=True
    )