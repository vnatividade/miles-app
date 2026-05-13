# Infrastructure — miles-app

# Objective

Definir infraestrutura inicial do MVP.

---

# Initial Requirements

O MVP deve:
- ser barato
- simples
- rápido para iterar
- fácil de operar

---

# Initial Infrastructure

## Backend

```txt
FastAPI
```

## Database

```txt
PostgreSQL
```

## Scheduler

```txt
APScheduler
```

## Cache / Queue

```txt
Redis (future)
```

## Containers

```txt
Docker
Docker Compose
```

---

# Deployment Strategy

## Recommended Initial Providers

- Railway
- Render
- Fly.io

---

# Environment Variables

## Examples

```txt
DATABASE_URL=
RESEND_API_KEY=
SCRAPER_TIMEOUT=
SCRAPER_RETRY_LIMIT=
DEFAULT_SEARCH_INTERVAL=
```

---

# Logging

Initial logging must include:
- scraper execution
- failures
- duration
- provider
- result count

---

# Monitoring

Initial monitoring should prioritize:
- scraper failures
- runtime duration
- notification delivery
- database connectivity

---

# Infrastructure Principles

## Keep Operational Cost Low

Avoid unnecessary infrastructure complexity.

## Prefer Simplicity

Single deployable application initially.

## Design For Evolution

The MVP must be evolvable without total rewrite.

---

# Future Infrastructure Evolution

Potential future additions:
- Kubernetes
- distributed workers
- dedicated scraping cluster
- observability stack
- proxy infrastructure
- browser pools
