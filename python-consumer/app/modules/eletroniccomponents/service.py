import json
import logging
from typing import Dict, Any, List

class EletronicComponents:
    _received_messages: List[Dict[str, Any]] = []
        
    @classmethod
    def get_all_messages(cls) -> List[Dict[str, Any]]:
        """
        Recupera todas as mensagens armazenadas
        """
        return cls._received_messages
    
    @classmethod
    def process_message(cls, body: bytes) -> Dict[str, Any]:
        """
        Processa uma mensagem recebida do RabbitMQ
        """
        try:
            message = json.loads(body)
            print(f" [x] Recebido: {message}")

            cls._received_messages.append(message)

            return message
        except Exception as e:
            logging.error(f"Erro ao processar mensagem: {str(e)}")
            return None