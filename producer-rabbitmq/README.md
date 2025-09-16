# RabbitMq - Producer / Consumer

---

## 1) Integrantes

* `Diogo Polastrine Duarte Silva` - RA: `01241114`
* `João Victor Barroso Melo` - RA: `01241125`

---

## 3) Passo a passo para subir o ambiente e executar ambos os serviços

> **Pré-requisitos**:
>
> * Docker e Docker Compose instalados
> * Ter instalado a IDE Intellij
> * Ter instalado o VSCode

**1. Clone o repositório abaixo**

```bash
https://github.com/Polastrine/rmq-stack-project
```

**2. Abra a pasta PRODUCER`**

* Troque portas expostas (`<PRODUCER_PORT>`, `<CONSUMER_PORT>`), nomes de serviços, variáveis de ambiente, e credenciais.

**3. Subir o ambiente via Docker Compose**

```bash
# build + start em background
docker compose up -d --build

# ver containers ativos
docker compose ps
```

**4. Verificar logs / status**

```bash
# logs do producer
docker compose logs -f producer

# logs do consumer
docker compose logs -f consumer

# parar e remover
docker compose down
```

**Executar localmente (sem Docker)** — exemplos genéricos, substitua pelos comandos do seu projeto:

* Producer (Spring Boot):

```bash
cd producer
./mvnw spring-boot:run   # ou: java -jar target/producer.jar
```

* Consumer (ex.: Node / Python):

```bash
cd consumer
# Node
npm install
npm start

# ou Python
pip install -r requirements.txt
python consumer.py
```

> **Onde substituir:** troque `producer`, `consumer`, e os comandos pelos nomes/entradas reais do seu projeto.

---

---

## 2) Como enviar uma mensagem de teste (endpoint do produtor)

**URL do endpoint de publicação**

```
POST http://localhost:8080/producer
```

**Método HTTP**: `POST`

**Exemplo de JSON a ser enviado**

```json
{
  "produto": "produto_1",
  "quantidade": 0
}
```

## 4) Exemplo de como enviar o POST de teste (curl)

Salve o JSON de exemplo em `message.json` e execute:

```bash
curl -X POST "http://<PRODUCER_HOST>:<PRODUCER_PORT>/<PRODUCER_PATH>" \
  -H "Content-Type: application/json" \
  -d @message.json
```

Ou inline:

```bash
curl -X POST "http://localhost:8080/xpto" -H "Content-Type: application/json" -d '{"messageId":"1","payload":{"nome":"Teste"}}'
```

---

## 5) Exemplo de retorno esperado (Producer)

Dependendo da implementação, o produtor pode retornar um `201 Created`, `200 OK` ou `202 Accepted`.

**Exemplo (201 Created)**

```
HTTP/1.1 201 Created
Content-Type: application/json

{
  "status": "published",
  "messageId": "123e4567-e89b-12d3-a456-426614174000"
}
```

**Exemplo (assíncrono - 202 Accepted)**

```
HTTP/1.1 202 Accepted
Content-Type: application/json

{ "status": "queued" }
```

> **Onde substituir:** adapte o texto de acordo com a resposta real do seu produtor.

---

## 6) Como verificar a mensagem no consumidor (GET / logs / UI)

### A) Endpoint GET do consumidor (exemplo)

```
GET http://<CONSUMER_HOST>:<CONSUMER_PORT>/<CONSUMER_PATH>/messages
```

**Exemplo concreto:**

```
GET http://localhost:8081/messages
```

**Resposta esperada (exemplo)**

```json
[
  {
    "messageId": "123e4567-e89b-12d3-a456-426614174000",
    "payload": { "nome": "Fulano de Tal", "descricao": "Mensagem de teste" },
    "receivedAt": "2025-09-16T12:35:10-03:00",
    "status": "consumed"
  }
]
```

### B) Verificação via logs do container / processo

```bash
# logs do consumer via docker
docker compose logs --follow consumer

# ou
docker logs -f <consumer_container_id>
```

Procure por linhas com indicação de consumo (ex.: `Received message`, `Processed message`, `payload:`).

### C) Verificação via broker (se aplicável)

Se você usa RabbitMQ/ActiveMQ/Kafka, pode checar a UI de gerenciamento do broker (ex.: RabbitMQ Management na porta `15672`) ou usar `rabbitmqctl` / `kafka-topics.sh` para inspeção de filas/topics.

---

## 7) Lista de placeholders — onde você deve substituir

Substitua todos os itens abaixo por valores do seu ambiente/projeto:

* `<NOME_COMPLETO_X>` — nome dos integrantes.
* `<RA_X>` — RA dos integrantes.
* `<PRODUCER_HOST>` — host onde o producer está rodando (ex.: `localhost` ou `producer-service`).
* `<PRODUCER_PORT>` — porta do producer (ex.: `8080`).
* `<PRODUCER_PATH>` — caminho do endpoint de publicação (ex.: `xpto` ou `api/publish`).
* `<CONSUMER_HOST>` — host do consumer.
* `<CONSUMER_PORT>` — porta do consumer (ex.: `8081`).
* `<CONSUMER_PATH>` — caminho do endpoint GET do consumer (ex.: `messages`).
* `<AUTH_TOKEN>` — token de autenticação, se usar.
* `<DOCKER_COMPOSE_FILE>` — caso não seja `docker-compose.yml`.
* `<PRODUCER_COMMAND>` / `<CONSUMER_COMMAND>` — comandos para rodar localmente sem containers.

---

## 8) Troubleshooting rápido

* **Não conecta no producer/consumer:** verifique portas e firewalls. Cheque `docker compose ps`.
* **Mensagem não chega ao consumer:** verifique se o broker (RabbitMQ/Kafka) está rodando e se as filas/topics estão corretas.
* **Erros de autenticação:** valide `Authorization` e variáveis de ambiente.
* **Ports ocupadas:** altere `<PRODUCER_PORT>` / `<CONSUMER_PORT>` no `docker-compose.yml`.

---

## 9) Contato / informações extras

Se desejar, substitua por um e-mail de contato:

* Responsável: `<SEU_NOME>` — `<SEU_EMAIL>`

---

**Fim do README**

*Observação final:* verifique todos os campos com `<>` antes de compactar e entregar o `.zip`. Boa sorte nos testes!
