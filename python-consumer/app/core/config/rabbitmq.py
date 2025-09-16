import pika
import json
import logging
from typing import Dict, Any, Callable

from app.core.config import settings

logger = logging.getLogger(__name__)

class RabbitMQClient:
    def __init__(self):
        self.connection = None
        self.channel = None
        self._connect()
    
    def _connect(self):
        """Estabelece conexão com o RabbitMQ"""
        try:
            
            parameters = pika.ConnectionParameters(
                host=settings.RABBITMQ_HOST,
                port=settings.RABBITMQ_PORT,
            )
            
            self.connection = pika.BlockingConnection(parameters)
            self.channel = self.connection.channel()
            
            self.channel.queue_declare(queue=settings.RABBITMQ_QUEUE, durable=True)
            
            logger.info(f"Conectado ao RabbitMQ em {settings.RABBITMQ_HOST}:{settings.RABBITMQ_PORT}")
        except Exception as e:
            logger.error(f"Erro ao conectar ao RabbitMQ: {str(e)}")
            raise
    
    def close(self):
        """Fecha a conexão com o RabbitMQ"""
        if self.connection and self.connection.is_open:
            self.connection.close()
            logger.info("Conexão com RabbitMQ fechada")
    
    def publish_message(self, message: Dict[str, Any], queue: str = None):
        """Publica uma mensagem na fila"""
        if queue is None:
            queue = settings.RABBITMQ_QUEUE
        
        try:
            self.channel.basic_publish(
                exchange='',
                routing_key=queue,
                body=json.dumps(message),
                properties=pika.BasicProperties(
                    delivery_mode=2,  # torna a mensagem persistente
                )
            )
            logger.info(f"Mensagem publicada na fila '{queue}': {message}")
            return True
        except Exception as e:
            logger.error(f"Erro ao publicar mensagem: {str(e)}")
            return False
    
    def consume_messages(self, callback: Callable, queue: str = None):
        """Consome mensagens de uma fila específica"""
        if queue is None:
            queue = settings.RABBITMQ_QUEUE
        
        try:
            self.channel.basic_consume(
                queue=queue,
                on_message_callback=callback,
                auto_ack=False
            )
            logger.info(f"Consumindo mensagens da fila '{queue}'")
            self.channel.start_consuming()
        except Exception as e:
            logger.error(f"Erro ao consumir mensagens: {str(e)}")
            raise


