# Scraping Strategy — miles-app

# Objective

Definir a estratégia operacional dos scrapers do miles-app.

---

# Initial Strategy

## Phase 1

Priorizar simplicidade e velocidade.

Utilizar:
- Requests para páginas simples
- Playwright para páginas dinâmicas

---

# Initial Providers

## Priority 1

- Smiles
- Azul

## Priority 2

- LATAM Pass

---

# Scraper Design

Cada provider deve ser independente.

Exemplo:

```txt
scrapers/
├── base.py
├── smiles.py
├── azul.py
└── latam.py
```

---

# Base Interface

Todos os scrapers devem seguir contrato único.

```python
search(criteria) -> list[RawSearchResult]
```

---

# Execution Flow

```txt
Scheduler
→ Provider Scraper
→ Raw Result Storage
→ Normalization
→ Matching
→ Notification
```

---

# Anti-Bot Considerations

Os providers irão bloquear automação eventualmente.

O sistema deve considerar:
- retries
- random delays
- user-agent rotation
- browser emulation
- session reuse
- proxy support futura

---

# Important Rule

Nunca acoplar lógica de negócio diretamente ao scraper.

O scraper deve apenas:
- capturar
- extrair
- retornar dados

---

# Failure Strategy

Falhas de um provider não devem derrubar os outros.

Cada execução deve:
- registrar logs
- registrar erros
- possuir timeout
- possuir retry controlado

---

# Future Evolution

## Future Features

- distributed workers
- proxy rotation
- captcha solving
- dynamic throttling
- browser pools
- intelligent scheduling
