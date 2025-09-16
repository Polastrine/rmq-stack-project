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
### 2. Inicie o produtor

**a) Abra a pasta "producer-rabbitmq" no Intellij**
- Inicie a aplicação

```bash
RUN ProducerRabbitmqApplication.java
```
- A dependência "spring-boot-docker-compose" iniciará automaticamente o container rabbitmq.
- Pronto, produtor inciado

### 3. Inicie o consumidor

**a) Abra a pasta "python-consumer" no VSCode**

**b) Com terminal aberto na pasta do projeto**
- Baixe as dependências com o comando abaixo
```bash
pip install -r requirements.txt
```
**c) Ainda no terminal**
- Inicie a aplicação
```bash
python3 main.py
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
Pedido enviada com successo {"produto": "produto_1", "quantidade": 0}
```

---

## 4) Como verificar as mensagens cosumidas (GET)

### URL do endpoint de GET (Listar mensagens)

```
GET http://localhost:8000/api/messages-event
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
