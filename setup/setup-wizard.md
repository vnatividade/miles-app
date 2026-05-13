# Setup Wizard — miles-app

## Purpose

Guide humans and agents through the required setup before implementation, deployment and monitoring.

This wizard must never store real secrets.

It only documents what must be configured and where.

---

# Setup Philosophy

Secrets, tokens and credentials must live in:

- local environment
- Railway variables
- GitHub secrets
- Datadog/Sentry dashboards
- MCP local configuration

Never commit real secrets to the repository.

---

# Required Accounts

## GitHub

Required for:
- repository access
- pull requests
- branch workflow
- optional GitHub Actions

Status:

```txt
[ ] GitHub repo configured
[ ] branch protection reviewed
[ ] PR template available
```

---

## Linear

Required for:
- tickets
- milestones
- execution visibility
- handoff

Status:

```txt
[ ] Linear project created
[ ] milestones created
[ ] initial tickets created
[ ] agent workflow documented
```

---

## Railway

Required for:
- application hosting
- PostgreSQL
- environments
- deployment logs

Status:

```txt
[ ] Railway project created
[ ] production environment created
[ ] staging environment created
[ ] PostgreSQL provisioned
[ ] backend service configured
[ ] healthcheck configured
```

---

## Datadog

Required for:
- logs
- APM
- metrics
- monitors
- dashboards
- technical monitoring agent

Status:

```txt
[ ] Datadog account created
[ ] API key generated
[ ] app instrumentation configured
[ ] monitors created
[ ] dashboard created
```

---

## Resend

Required for:
- email notifications

Status:

```txt
[ ] Resend account created
[ ] API key generated
[ ] sending domain configured
[ ] sender validated
```

---

# Required Environment Variables

## Application

```txt
APP_ENV=
APP_NAME=miles-app
LOG_LEVEL=
```

---

## Database

```txt
DATABASE_URL=
```

Optional Railway Postgres variables:

```txt
PGHOST=
PGPORT=
PGUSER=
PGPASSWORD=
PGDATABASE=
```

---

## Scraping

```txt
SCRAPER_TIMEOUT=
SCRAPER_RETRY_LIMIT=
DEFAULT_SEARCH_INTERVAL=
```

---

## Notifications

```txt
RESEND_API_KEY=
NOTIFICATION_FROM_EMAIL=
```

---

## Observability

```txt
DD_API_KEY=
DD_SITE=
DD_SERVICE=miles-app
DD_ENV=
DD_VERSION=
```

---

## Agent / MCP Local Config

Do not commit local MCP configs.

Expected local integrations:

```txt
GitHub MCP / connector
Linear MCP / connector
Codex local config
Cursor local config
Claude local config
```

---

# Environment Strategy

Recommended environments:

```txt
local
staging
production
preview
```

---

# Setup Sequence

## 1. Local Development

```txt
[ ] clone repo
[ ] install dependencies
[ ] create .env from .env.example
[ ] run app locally
[ ] validate /health
```

---

## 2. Database

```txt
[ ] provision Postgres
[ ] configure DATABASE_URL
[ ] run migrations
[ ] validate connection
```

---

## 3. Railway

```txt
[ ] create Railway project
[ ] connect GitHub repo
[ ] configure env vars
[ ] deploy staging
[ ] validate /health
```

---

## 4. Observability

```txt
[ ] configure Datadog env vars
[ ] enable logs
[ ] enable APM
[ ] create monitors
[ ] validate test error/log
```

---

## 5. Notifications

```txt
[ ] configure Resend
[ ] validate sender
[ ] send test email
```

---

## 6. Agentic Workflow

```txt
[ ] verify Linear access
[ ] verify GitHub access
[ ] verify Codex reads AGENTS.md
[ ] verify skills are discoverable
[ ] verify PR template is used
```

---

# Done Criteria

Setup is complete when:

- local app runs
- staging deploy works
- database connection works
- `/health` responds
- logs are visible
- Datadog receives data
- Linear tickets are connected to PR workflow
- no secrets are committed

---

# Important Rule

If setup requires a secret, document the variable name and destination.

Never document the secret value.
