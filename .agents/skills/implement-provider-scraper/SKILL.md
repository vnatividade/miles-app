# Skill — Implement Provider Scraper

## Purpose

Implement a provider scraper safely and consistently.

---

# Required Context

Before implementation read:

```txt
AGENTS.md
architecture/scraping-strategy.md
architecture/architecture.md
assigned Linear ticket
```

---

# Objective

Create isolated provider scrapers that:
- capture flight opportunity data
- preserve raw payloads
- support normalization
- fail safely

---

# Recommended Structure

```txt
src/scrapers/
├── base.py
├── smiles.py
├── azul.py
└── latam.py
```

---

# Responsibilities

Each provider scraper should:

- receive search criteria
- execute provider request
- parse provider response
- preserve raw payload
- return normalized intermediate structures

---

# Important Rules

## 1. No Business Logic

Scrapers should not contain alert matching logic.

## 2. Preserve Raw Provider Data

Always preserve raw payloads before normalization.

## 3. Provider Isolation

Provider failures must not break the entire system.

## 4. Anti-Bot Awareness

Assume providers may:
- throttle
- change layouts
- introduce captchas
- block requests

---

# Anti-Patterns

Avoid:
- tightly coupled providers
- provider-specific hacks leaking into shared layers
- hidden parsing assumptions
- silent retries without logging

---

# Expected Outputs

- provider scraper
- normalized structures
- timeout handling
- retry handling
- logging hooks
- provider operational notes
