# Architecture — miles-app

## Purpose

Este documento define a arquitetura inicial do miles-app para o MVP.

O objetivo é criar uma base simples, evolutiva e operacionalmente segura para:
- cadastrar alertas
- executar buscas periódicas
- capturar resultados de programas de milhas
- normalizar dados
- comparar oportunidades com preferências do usuário
- enviar notificações

---

# High-Level Architecture

```txt
User Interface / Admin Form
        ↓
FastAPI Backend
        ↓
PostgreSQL
        ↓
Scheduler
        ↓
Scraper Workers
        ↓
Raw Results + Normalized Results
        ↓
Matching Engine
        ↓
Notification Service
```

---

# Core Components

## API Backend

Responsável por:
- criar alertas
- listar alertas
- ativar/desativar alertas
- consultar resultados
- consultar histórico de notificações

Stack sugerida:
- Python
- FastAPI
- Pydantic
- SQLAlchemy

---

## Scheduler

Responsável por disparar buscas em intervalos configuráveis.

No MVP, priorizar simplicidade:
- APScheduler para início rápido
- Celery + Redis somente se houver necessidade real de escala

---

## Scraper Workers

Cada programa deve ter um scraper isolado.

Exemplo:

```txt
scrapers/
├── smiles.py
├── azul.py
└── latam.py
```

Cada scraper deve implementar uma interface comum:

```txt
search(criteria) -> list[RawSearchResult]
```

---

## Normalization Layer

Responsável por converter respostas diferentes em um formato único.

Exemplo:
- milhas
- taxas
- datas
- origem
- destino
- companhia
- programa
- disponibilidade

---

## Matching Engine

Responsável por comparar resultados capturados com alertas ativos.

Critérios iniciais:
- origem
- destino
- data dentro do range
- milhas <= máximo configurado
- taxa <= máximo configurado
- classe de cabine
- quantidade de passageiros

---

## Notification Service

Canal inicial:
- e-mail

Canais futuros:
- WhatsApp
- Telegram
- push notification

---

# Architectural Principles

## 1. Modular Scrapers

Scrapers quebram. Eles devem ser isolados para não derrubar o sistema inteiro.

## 2. Raw Data Preservation

Sempre salvar o dado bruto capturado antes da normalização.

## 3. Traceability

Todo resultado precisa saber:
- de onde veio
- quando foi capturado
- qual scraper gerou
- qual input originou a busca

## 4. Simple First

Não usar arquitetura distribuída antes de provar valor.

## 5. Replaceable Components

Cada parte deve poder ser trocada sem reescrever o sistema inteiro.

---

# Initial Stack

```txt
Language: Python 3.11+
API: FastAPI
Database: PostgreSQL
Scheduler: APScheduler
Scraping: Playwright + Requests
Email: Resend
Container: Docker
Deployment: Railway, Render or Fly.io
```

---

# Future Evolution

Quando o MVP validar valor, evoluir para:
- filas assíncronas
- workers separados
- Redis
- observabilidade avançada
- proxy strategy
- painel web
- scoring de oportunidade
