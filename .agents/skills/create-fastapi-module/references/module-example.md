# FastAPI Module Example

```txt
src/
└── alerts/
    ├── routes.py
    ├── schemas.py
    ├── service.py
    ├── repository.py
    └── models.py
```

---

# Example Responsibilities

## routes.py

```python
router = APIRouter(prefix="/alerts")
```

Contains:
- endpoints
- request validation
- response mapping

---

## service.py

Contains:
- orchestration
- business flow
- validation coordination

---

## repository.py

Contains:
- database access
- persistence operations

---

## schemas.py

Contains:
- request models
- response models
- validation contracts

---

## models.py

Contains:
- SQLAlchemy models
- domain entities
```
