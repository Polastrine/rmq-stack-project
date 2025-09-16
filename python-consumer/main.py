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

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

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


# Inclusão dos routers
app.include_router(eletroniccomponents_controller, prefix="/api/v1")

# Função para iniciar o servidor
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=True
    )