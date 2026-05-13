# Skill — Deploy to Railway

## Purpose

Prepare and execute Railway deployment workflows for miles-app.

---

# Required Context

Before deployment work, read:

```txt
AGENTS.md
architecture/infra.md
execution/workflow.md
.codex/hooks/before-pr.md
assigned Linear ticket
```

---

# Objective

Enable safe, repeatable Railway deployments while preserving operational clarity.

---

# Responsibilities

This skill covers:

- Railway project setup guidance
- environment planning
- service configuration
- Dockerfile readiness
- healthcheck planning
- environment variable mapping
- deployment checklist
- rollback notes

---

# Railway Environments

Recommended environments:

```txt
production
staging
preview/pr-environments
```

---

# Required Variables

Expected variables:

```txt
DATABASE_URL=
RESEND_API_KEY=
SCRAPER_TIMEOUT=
SCRAPER_RETRY_LIMIT=
DEFAULT_SEARCH_INTERVAL=
APP_ENV=
LOG_LEVEL=
```

Never commit real secrets.

Use `.env.example` only.

---

# Deployment Checklist

Before deploy:

- [ ] Dockerfile exists
- [ ] app starts successfully
- [ ] healthcheck endpoint exists
- [ ] required env vars documented
- [ ] database connection validated
- [ ] logs are visible
- [ ] rollback path is documented

---

# Healthcheck Standard

The app should expose:

```txt
GET /health
```

Expected response:

```json
{
  "status": "ok"
}
```

---

# Anti-Patterns

Avoid:

- deploying without healthcheck
- committing Railway tokens
- relying on local-only config
- manual undocumented deployment steps
- mixing staging and production variables

---

# Expected Outputs

- Railway deployment instructions
- environment variable mapping
- deployment checklist
- rollback notes
- docs updates when infra behavior changes
