from pydantic import BaseModel
from typing import Dict, Any, List, Optional

class MessageListResponse(BaseModel):
    """Schema para lista de mensagens"""
    messages: List[Dict[str, Any]]
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "messages": [
                    {"componente": "DHT11", "quantidade": 5},
                    {"componente": "LED", "quantidade": 10}
                ]
            }
        }
    }

