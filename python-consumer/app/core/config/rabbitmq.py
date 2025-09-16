import pika
import logging
from typing import Callable

from app.core.config import settings

logger = logging.getLogger(__name__)

class RabbitMQClient:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.queue = settings.RABBITMQ_QUEUE
        self._connect()

    
    
    def _connect(self):
        """Estabelece conexão com o RabbitMQ"""
        credentials = pika.PlainCredentials(
            username=settings.RABBITMQ_USER,
            password=settings.RABBITMQ_PASSWORD
        )
        
        parameters = pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            credentials=credentials,
            heartbeat=600,
            blocked_connection_timeout=300
        )
        
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()
        
        self.channel.queue_declare(queue=self.queue, durable=True)
        logger.info(f"Fila '{self.queue}' declarada")
        
        logger.info(f"Conectado ao RabbitMQ em {settings.RABBITMQ_HOST}:{settings.RABBITMQ_PORT}")
    
    def close(self):
        """Fecha a conexão com o RabbitMQ"""
        if self.connection and self.connection.is_open:
            self.connection.close()
            logger.info("Conexão com RabbitMQ fechada")
    
    def consume_messages(self, callback: Callable, queue: str = None):
        """Consome mensagens de uma fila específica (bloqueante)
        
        Esta é a implementação simples conforme a documentação do RabbitMQ
        """
        if queue:
            self.queue = queue
            
        self.channel.basic_consume(
            queue=self.queue,
            on_message_callback=callback,
            auto_ack=True  
        )
        
        logger.info(f"Aguardando mensagens da fila '{self.queue}'. Para sair pressione CTRL+C")
        
        self.channel.start_consuming()
        


