# Web Frameworks

This module explores Flask contexts and FastAPI/Pydantic behavior.

## Puzzles

### 1. Flask Request Context (`puzzle_01_flask_context.py`)

**Question:** What happens when you access Flask's `g` object outside a request?

**Answer:**
```
=== Test normal request ===
Set g.user = Alice
Response: Hello, Alice!

=== Test manual access ===
Error accessing g outside request: RuntimeError: Working outside of request context.
```

**Explanation:**

Flask uses context locals to make request-specific data available:
- `g`: request-scoped data
- `request`: the current request object

These are only available during request processing. Outside a request context, accessing them raises `RuntimeError`.

Use `app.app_context()` or `app.test_request_context()` for testing.

**Key Takeaway:** Flask's context system ensures thread-safety by isolating request data.

**References:**
- [Flask Docs - Context Locals](https://flask.palletsprojects.com/en/3.0.x/appcontext/)
- [Flask Docs - g Object](https://flask.palletsprojects.com/en/3.0.x/api/#flask.g)

---

### 2. FastAPI Dependency Injection (`puzzle_02_fastapi_di.py`)

**Question:** What's the difference between return and yield in FastAPI dependencies?

**Answer:**
- **Return:** Function runs on each request, no cleanup guaranteed
- **Yield:** Function runs on each request, cleanup code after yield runs after response is sent

With `yield`:
1. Code before yield runs before the endpoint
2. Code after yield runs after the response is sent (even if exception)
3. Perfect for resource management (DB connections, file handles)

**Key Takeaway:** Use `yield` for dependencies that need cleanup (database, file handles).

**References:**
- [FastAPI Docs - Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
- [FastAPI Docs - Yield Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/)

---

### 3. Pydantic Validation (`puzzle_03_pydantic_validation.py`)

**Question:** How does Pydantic handle type coercion?

**Answer:**
```
=== String to int coercion ===
Created user: id=1 name='Alice' age=25

=== Passing dict to model ===
Created user from dict: id=2 name='Bob' age=30

=== Invalid data ===
Error: ValidationError: 2 validation errors for User

=== Extra fields (default behavior) ===
Created user: id=4 name='Carol' age=20

=== Strict mode ===
Error: ValidationError: Input should be a valid integer
```

**Explanation:**

- **Coercion (default):** Pydantic coerces strings to ints, floats to ints if valid
- **Validation:** Invalid values (empty name, negative age) raise `ValidationError`
- **Extra fields:** By default, extra fields are ignored
- **Strict mode:** No coercion - types must match exactly

**Key Takeaway:** Understand Pydantic's coercion behavior - it's convenient but can hide bugs.

**References:**
- [Pydantic Docs - Coercion](https://docs.pydantic.dev/latest/concepts/coercion/)
- [Pydantic Docs - Strict Mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
