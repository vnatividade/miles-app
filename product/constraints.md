# Constraints — miles-app

# MVP Constraints

## 1. Narrow Scope

O MVP deve permanecer extremamente focado.

Não adicionar funcionalidades fora do objetivo principal de:
- monitorar
- detectar
- alertar

---

# 2. Avoid Premature Complexity

Evitar:
- microservices
- kubernetes
- arquitetura distribuída
- event sourcing
- multi-cloud
- overengineering

---

# 3. Scraper Resilience

Scrapers irão quebrar.

A arquitetura deve assumir:
- mudanças frequentes de layout
- captchas
- bloqueios
- rate limits

---

# 4. Data Quality First

Dados incorretos destroem confiança.

Priorizar:
- precisão
- consistência
- rastreabilidade

---

# 5. Fast Iteration

A velocidade de aprendizado é mais importante que perfeição arquitetural inicial.

---

# 6. Operational Simplicity

O sistema deve ser simples de:
- rodar
- debugar
- monitorar
- ajustar
- evoluir
