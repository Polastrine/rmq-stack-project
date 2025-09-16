from pydantic import BaseModel
from typing import Dict, Any, List, Optional


class MessageEventResponse(BaseModel):
    """Schema para resposta de mensagem de evento"""
    component: str
    value: float
    unit: str
    timestamp: str
    
    class Config:
        schema_extra = {
            "example": {
                "component": "temperature_sensor",
                "value": 25.5,
                "unit": "celsius",
                "timestamp": "2025-09-15T14:30:00Z"
            }
        }

