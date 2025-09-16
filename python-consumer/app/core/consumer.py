import logging
import sys
import os
from app.core.config.rabbitmq import RabbitMQClient
from app.modules.eletroniccomponents.service import EletronicComponents

logger = logging.getLogger(__name__)

class RabbitMQConsumer:
    _instance = None
    _client = None
    
    def __new__(cls):
        cls._instance = super(RabbitMQConsumer, cls).__new__(cls)
        return cls._instance
    
    @classmethod
    def start_consumer(cls):
        """
        Inicia o consumidor de mensagens RabbitMQ seguindo o exemplo da documentação.
        Este método é bloqueante e deve ser executado em uma thread separada ou processo.
        """
        # Criar conexão com RabbitMQ
        cls._client = RabbitMQClient()
        logger.info("Consumidor RabbitMQ iniciado com sucesso")
        
        cls._client.consume_messages(callback=EletronicComponents.callback)

        
    @classmethod
    def stop_consumer(cls):
        """Para o consumidor de mensagens"""
        if cls._client:
            cls._client.close()
            logger.info("Consumidor RabbitMQ encerrado com sucesso")
            
    @classmethod
    def run(cls):
        """
        Executa o consumidor seguindo o padrão da documentação do RabbitMQ
        """
        try:
            cls.start_consumer()
        except KeyboardInterrupt:
            logger.info('Consumidor interrompido')
            try:
                cls.stop_consumer()
                sys.exit(0)
            except SystemExit:
                os._exit(0)
    
