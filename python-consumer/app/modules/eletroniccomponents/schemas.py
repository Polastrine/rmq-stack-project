from pydantic import BaseModel
from typing import Dict, Any, List, Optional


class MessageEventResponse(BaseModel):
    """Schema para resposta de mensagem de evento"""
    # Usando model_config que é a forma recomendada no Pydantic v2
    # ao invés de Config com schema_extra
    componente: Optional[str] = None
    quantidade: Optional[int] = None
    message: Optional[str] = None
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "componente": "DHT11",
                "quantidade": 5
            }
        }
    }


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

