# Web Frameworks

This module explores Flask contexts and FastAPI/Pydantic behavior—the hidden mechanisms that make these frameworks work.

## Topics Covered

### Flask Request Context
Flask uses thread-local storage to provide request-specific data via `g` and `request` objects. Understanding context locals explains why these aren't available outside request handlers.

### FastAPI Dependency Injection
FastAPI's dependency system supports two patterns: `return` for simple values and `yield` for resources needing cleanup. The `yield` pattern ensures teardown code runs after the response is sent—even if an exception occurs.

### Pydantic Validation
Pydantic provides automatic type coercion (convenient but potentially dangerous) and strict mode (no coercion). Understanding the difference helps avoid subtle bugs where strings silently become integers.

## Running the Puzzles

```bash
uv run python 05-web-frameworks/puzzle_01_flask_context.py
uv run python 05-web-frameworks/puzzle_02_fastapi_di.py
uv run python 05-web-frameworks/puzzle_03_pydantic_validation.py
```
