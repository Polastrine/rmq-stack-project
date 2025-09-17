import pika, logging, sys, os, threading
from typing import Callable

from app.core.config import settings
from app.modules.eletroniccomponents.service import EletronicComponents

class RabbitMQClient:
    def __init__(self):
        self.connection = None
        self.channel = None
        self.queue = settings.RABBITMQ_QUEUE
        self.consumer_thread = None
    
    def connect(self):
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
        print(f"Conectado ao RabbitMQ em {settings.RABBITMQ_HOST}:{settings.RABBITMQ_PORT}")
    
    def callback(self, ch, method, properties, body):
        EletronicComponents.process_message(body)
    
    def _start_consuming(self):
        """Método que será executado em uma thread separada"""
        try:
            self.channel.start_consuming()
        except Exception as e:
            logging.error(f"Erro no consumidor RabbitMQ: {e}")
            
    def consume_messages(self):
        self.channel.basic_consume(
            queue=self.queue,
            on_message_callback=self.callback,
            auto_ack=True  
        )

        print(f"Aguardando mensagens da fila '{self.queue}'. Para sair pressione CTRL+C")
        
        # Inicia o consumo em uma thread separada
        self.consumer_thread = threading.Thread(target=self._start_consuming)
        self.consumer_thread.daemon = True  # Isso permite que a thread seja encerrada quando o programa principal terminar
        self.consumer_thread.start()