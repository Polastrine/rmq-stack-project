import threading
import logging
from app.core.config.rabbitmq import RabbitMQClient
from app.modules.eletroniccomponents.service import EletronicComponents

logger = logging.getLogger(__name__)

class RabbitMQConsumer:
    _instance = None
    _consumer_thread = None
    _client = None
    _is_running = False
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RabbitMQConsumer, cls).__new__(cls)
        return cls._instance
    
    @classmethod
    def start_consumer(cls):
        """Inicia o consumidor de mensagens RabbitMQ em uma thread separada"""
        cls._client = RabbitMQClient()
        cls._is_running = True
        
        cls._consumer_thread = threading.Thread(
            target=cls._run_consumer,
            daemon=True  # Thread será encerrada quando o programa principal terminar
        )
        cls._consumer_thread.start()
        
        logger.info("Consumidor RabbitMQ iniciado com sucesso")
            
        
    
    @classmethod
    def _run_consumer(cls):
        """Método executado na thread do consumidor"""
        logger.info("Iniciando consumo de mensagens RabbitMQ")
        cls._client.consume_messages(callback=EletronicComponents.callback)
        
    
    @classmethod
    def stop_consumer(cls):
        """Para o consumidor de mensagens"""
        if not cls._is_running:
            return
            
        if cls._client:
            cls._client.close()
            cls._is_running = False
            logger.info("Consumidor RabbitMQ encerrado com sucesso")
    
