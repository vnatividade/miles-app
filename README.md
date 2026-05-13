# miles-app

Aplicativo para organizar, acompanhar e otimizar o uso de milhas, pontos e benefícios de programas de fidelidade.

## Objetivo

Centralizar informações de programas de milhas, saldo de pontos, validade, oportunidades de resgate e estratégias para maximizar valor.

## Status

Projeto em estágio inicial.

## Backend local

Base inicial do backend criada com FastAPI para desenvolvimento local.

### Setup

```bash
./setup/bootstrap-codex.sh
```

O script cria `.env` a partir de `.env.example`, quando necessário, e instala as dependências de desenvolvimento.

### Rodar localmente

```bash
uvicorn miles_app.main:app --reload
```

Healthcheck:

```bash
curl http://localhost:8000/health
```

Resposta esperada:

```json
{"status":"ok"}
```

### Docker local

```bash
docker compose up --build
```

O `docker-compose.yml` inclui um PostgreSQL local para preparação de desenvolvimento, mas a aplicação ainda não depende de uma conexão real com banco.

### Checks

```bash
./setup/maintenance-codex.sh
```

Executa lint e testes locais.

## Próximos passos

- Definir visão do produto
- Mapear funcionalidades do MVP
- Estruturar arquitetura inicial
- Criar backlog técnico
- Definir stack do projeto
