# Skill — Apply Engineering Standards

## Purpose

Ensure generated code follows the engineering standards defined for miles-app.

---

# Required Context

Read:

```txt
architecture/engineering-standards.md
AGENTS.md
assigned Linear ticket
```

---

# Objective

Apply the project's architectural and engineering standards pragmatically.

---

# Responsibilities

This skill covers:

- layered architecture guidance
- DDD guidance
- dependency injection guidance
- SOLID validation
- design pattern validation
- Swagger/OpenAPI completeness
- testing quality validation

---

# Validation Checklist

## Architecture

- is the architecture proportional to the problem?
- is layering clear?
- are boundaries explicit?

## DDD

- is there real domain behavior?
- are entities/value objects/services justified?

## Dependency Injection

- are dependencies explicit?
- are infrastructure concerns injectable?

## Design Patterns

- is the pattern solving a real problem?
- is there accidental complexity?

## FastAPI

- do endpoints contain proper OpenAPI metadata?
- are request/response contracts explicit?

## Testing

- do tests follow Arrange/Act/Assert?
- are behaviors tested instead of implementation details?

---

# Anti-Patterns

Avoid:

- architecture for architecture's sake
- unnecessary hexagonal complexity
- generic managers/factories everywhere
- hidden singleton state
- undocumented endpoints
- tests coupled to implementation details

---

# Expected Outputs

- architectural reasoning
- standards validation
- suggested improvements
- code quality notes
- testing recommendations
