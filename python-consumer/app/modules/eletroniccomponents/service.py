import json
import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class EletronicComponents:
    _received_messages: List[Dict[str, Any]] = []
   
    @classmethod
    def callback(cls, ch, method, properties, body):
        """
        Callback para processar mensagens recebidas
        Seguindo o exemplo da documentação do RabbitMQ
        """
        try:
            message = json.loads(body)
            print(f" [x] Recebido: {message}")
            
            cls._received_messages.append(message)
            
            return message
        except Exception as e:
            logger.error(f"Erro ao processar mensagem: {str(e)}")
            return None

        
    @classmethod
    def get_all_messages(cls) -> List[Dict[str, Any]]:
        """
        Recupera todas as mensagens armazenadas
        """
        return cls._received_messages