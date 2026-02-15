# Building Challenges

This module contains hands-on implementations of core Python patterns—building familiar tools from scratch to deeply understand how they work.

## Topics Covered

### Retry Decorator
Implementing a decorator with configurable parameters demonstrates the decorator factory pattern. Understanding `functools.wraps` is essential for preserving function metadata.

### Simple Router
Building a WSGI-compatible router shows how Flask and FastAPI work under the hood. Implementing `__call__` makes classes callable, and understanding the WSGI interface reveals how web servers communicate with Python applications.

### Custom Future
Implementing a Promise/Future with callbacks demonstrates thread-safe state management, the observer pattern, and how async libraries handle asynchronous results.

## Running the Challenges

```bash
uv run python 06-building-challenges/challenge_01_retry_decorator.py
uv run python 06-building-challenges/challenge_02_simple_router.py
uv run python 06-building-challenges/challenge_03_custom_future.py
```
