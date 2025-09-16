#!/usr/bin/env python
import sys
import os
import logging
from app.core.consumer import RabbitMQConsumer

# Configuração básica de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger(__name__)

def main():
    """
    Função principal para iniciar o consumidor de mensagens RabbitMQ
    """
    print(' [*] Aguardando mensagens. Para sair pressione CTRL+C')
    # Inicia o consumidor usando a implementação simples
    RabbitMQConsumer.run()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Consumidor interrompido')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
