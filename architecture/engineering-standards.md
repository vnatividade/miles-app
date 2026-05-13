# Engineering Standards — miles-app

## Purpose

Define the engineering principles that must guide all code generated for miles-app.

These standards are meant to increase maintainability, clarity and evolvability without creating unnecessary architecture ceremony.

---

# Core Principle

Use strong engineering practices pragmatically.

The goal is not to force enterprise patterns everywhere.

The goal is to create code that is:

- understandable
- testable
- modular
- evolvable
- explicit
- safe for agents and humans to continue

---

# Architectural Direction

## Default Architecture

Prefer layered architecture for the MVP:

```txt
API layer
→ application/service layer
→ domain layer
→ infrastructure layer
```

---

# When To Use DDD

Use DDD concepts when there is meaningful domain behavior.

Examples:

- alerts
- opportunities
- matching rules
- feedback
- notifications
- provider search executions

Recommended tactical patterns:

- entities
- value objects
- repositories
- domain services
- application services
- factories when object creation becomes non-trivial

Do not overuse DDD for simple CRUD or configuration code.

---

# When To Use Hexagonal Architecture

Use hexagonal architecture only when it creates real separation of concerns.

Good candidates:

- scraper providers
- notification providers
- observability adapters
- persistence adapters
- external APIs

Avoid applying hexagonal architecture mechanically to every folder.

---

# Monorepo Guidance

A monorepo may be used if the project grows into multiple workloads.

Potential workloads:

```txt
backend-api
scheduler
scraper-worker
frontend
```

Do not create multiple workloads before there is a real operational need.

Start simple. Split when it improves deployment, ownership or runtime isolation.

---

# SOLID Principles

Apply SOLID pragmatically:

## Single Responsibility

Each module/class/function should have one clear reason to change.

## Open/Closed

Use interfaces/protocols when extension is expected, especially for providers.

## Liskov Substitution

Provider implementations must respect shared contracts.

## Interface Segregation

Avoid large generic interfaces.

## Dependency Inversion

Application/domain code should depend on abstractions, not concrete infrastructure.

---

# Dependency Injection

Dependency injection is required for:

- services
- repositories
- external providers
- configuration
- notification adapters
- scraper providers

Prefer explicit dependency injection.

Avoid hidden globals and hardcoded infrastructure dependencies.

In FastAPI, use dependency providers intentionally and keep them simple.

---

# Design Patterns

Use design patterns when they solve a real problem.

Recommended patterns:

## Factory

Use for complex object/provider creation.

Example:

- scraper provider factory
- notification provider factory

## Strategy

Use for interchangeable algorithms or providers.

Example:

- matching strategies
- provider search strategies
- notification channel strategies

## Repository

Use to isolate persistence access.

## Adapter

Use for external systems.

Example:

- Railway
- Datadog
- Resend
- airline providers

## Singleton

Avoid by default.

Use only for safe stateless shared resources or controlled lifecycle objects.

Do not use singleton as a global state shortcut.

---

# FastAPI Endpoint Standards

Every endpoint must include:

- explicit request model
- explicit response model
- summary
- description
- response descriptions
- status codes
- tags
- validation rules
- examples when useful

Swagger/OpenAPI documentation is part of the deliverable.

An endpoint without good OpenAPI metadata is incomplete.

---

# Testing Standards

Tests must follow the 3A pattern:

```txt
Arrange
Act
Assert
```

Every non-trivial behavior should include tests.

Prioritize:

- domain behavior tests
- service tests
- API contract tests
- provider contract tests

Avoid tests that only assert implementation details.

---

# Code Style

Prefer:

- explicit names
- small functions
- typed signatures
- clear modules
- predictable imports
- low coupling

Avoid:

- magic abstractions
- generic managers for everything
- hidden side effects
- premature inheritance trees
- clever code

---

# Agent Rule

When generating code, agents must explain which architectural style and patterns were used and why.

If a pattern is not needed, do not force it.

Good engineering is not decoration.
