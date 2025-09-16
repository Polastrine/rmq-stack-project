# RabbitMq - Producer / Consumer

---

## 1) Integrantes

* `Diogo Polastrine Duarte Silva` - RA: `01241114`
* `João Victor Barroso Melo` - RA: `01241125`

---

## 2) Passo a passo para subir o ambiente e executar ambos os serviços

> **Pré-requisitos**:
>
> * Docker e Docker Compose instalados
> * Ter instalado a IDE Intellij
> * Ter instalado o VSCode
> * Ter instalado Python 3
> * Ter instalado JDK 21

### 1. Clone o repositório abaixo

```bash
https://github.com/Polastrine/rmq-stack-project
```
### 2. Inicie o produtor + RabbitMq

**a) Abra a pasta "producer-rabbitmq" no Intellij**
- Inicie a aplicação

```bash
RUN ProducerRabbitmqApplication.java
```
- A dependência "spring-boot-docker-compose" iniciará automaticamente o container rabbitmq.
- Pronto, produtor inciado

### 3. Inicie o consumidor

**a) Abra a pasta "python-consumer" no VSCode**

**b) Crie um .env na raiz do projeto, com as seguintes informações:**
```bash
PROJECT_NAME=RabbitMQ Consumer API
PROJECT_DESCRIPTION=API to consume messages from RabbitMQ
PROJECT_VERSION=0.1.0
PROJECT_DOCS_URL=/docs
PROJECT_REDOC_URL=/redoc
PROJECT_OPENAPI_URL=/openapi.json
API_HOST=0.0.0.0
API_PORT=8000

RABBITMQ_HOST=localhost
RABBITMQ_PORT=5672
RABBITMQ_QUEUE=queue.pedido
RABBITMQ_USER=myuser
RABBITMQ_PASSWORD=secret
```
**c) Com terminal aberto na pasta do projeto**
- Baixe as dependências com o comando abaixo
```bash
pip install -r requirements.txt
```
**d) Ainda no terminal**
- Inicie a aplicação
```bash
python main.py
```
- Pronto, consumidor iniciado

---


## 3) Como enviar uma mensagem para o rabbitmq (endpoint do produtor)

### URL do endpoint de publicação

```
POST http://localhost:8080/producer
```

### Método HTTP: `POST`

### Exemplo de JSON a ser enviado

```json
{
  "produto": "produto_1",
  "quantidade": 0
}
```

### Retorno esperado
```string
Pedido enviado com successo {"produto": "produto_1", "quantidade": 0}
```

---

## 4) Como verificar as mensagens cosumidas (GET)

### URL do endpoint de GET (Listar mensagens)

```
GET http://localhost:8000/api/v1/electronic-components/messages-event
```

### Método HTTP: `GET`

### Retorno esperado
```json
{
  "messages": [
    {"produto": "produto1", "quantidade": 5},
    {"produto": "produto2", "quantidade": 10}
  ]
}
```
---
