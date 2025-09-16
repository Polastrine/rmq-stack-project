from typing import Dict, Any

class EletronicComponents:
   
    _messages = []

    @classmethod
    def get_message_event(cls) -> Dict[str, Any]:
        """
        Recupera a última mensagem de evento
        """
        if cls._messages:
            return cls._messages[-1]
        return {}