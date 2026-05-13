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
search(criteria: ScraperSearchCriteria) -> ScraperSearchResult
```

Implementação base:

```txt
src/miles_app/scrapers/base.py
```

---

# Provider Contract

Cada provider futuro deve implementar:

```python
BaseScraper._search_once(criteria, config) -> ScraperSearchResult
```

O método público `search(...)` é herdado de `BaseScraper` e padroniza:

- número de tentativas
- retry de falhas retryable
- backoff fixo entre tentativas
- erro final padronizado
- logging de retry

---

# Search Input Structure

O contrato de entrada é `ScraperSearchCriteria`.

Campos iniciais:

```txt
origin_airport
destination_airport
start_date
end_date
flexibility_days
cabin_class
passengers
nonstop_only
```

Regras:

- aeroportos são normalizados para uppercase
- `end_date` deve ser maior ou igual a `start_date`
- `passengers` deve estar entre 1 e 9
- `flexibility_days` deve estar entre 0 e 30
- `cabin_class` deve ser `economy`, `premium_economy`, `business` ou `first`

Campos como `max_miles` e `max_cash_fee` pertencem ao matching/alert engine,
não ao scraper. O scraper captura disponibilidade e preços; ele não decide se
uma oportunidade é boa para um alerta.

---

# Output Contracts

## RawScraperResult

Preserva o dado bruto ou registro extraído do provider.

Campos:

```txt
provider
search_input
raw_payload
source_url
captured_at
```

## NormalizedScraperResult

Fornece estrutura intermediária normalizada para persistência e matching.

Campos:

```txt
provider
airline
origin
destination
departure_date
return_date
miles_price
cash_fee
currency
cabin_class
stops
flight_duration
availability
source_url
captured_at
```

## ScraperSearchResult

Agrupa o resultado de uma execução de provider:

```txt
provider
criteria
raw_results
normalized_results
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

Configuração padrão:

```txt
timeout_seconds: 30
retry_limit: 3
retry_backoff_seconds: 1.0
```

Falhas retryable devem lançar `ScraperProviderError(retryable=True)`.

Falhas não retryable, como captcha obrigatório ou contrato inválido do provider,
devem lançar `ScraperProviderError(retryable=False)`.

Após esgotar tentativas, a execução pública lança `ScraperExecutionFailed`.

---

# Future Evolution

## Future Features

- distributed workers
- proxy rotation
- captcha solving
- dynamic throttling
- browser pools
- intelligent scheduling
