# Python Interview Prep

Advanced Python puzzles and solutions for interview preparation.

## Overview

This repository contains a collection of "Puzzle vs. Solution" challenges covering:
- Core Python mechanics (mutability, scoping, arguments)
- OOP internals (MRO, metaclasses, dunder methods)
- Generators and iterators
- AsyncIO and concurrency
- Web frameworks (Flask/FastAPI)
- Building challenges (implement core patterns from scratch)

## Structure

```
python-interview-prep/
├── 01-core-mechanics/      # Mutable defaults, closures, LEGB scope
├── 02-oop-internals/       # MRO, class vs instance vars, __new__ vs __init__
├── 03-generators-iterators/# Yield, yield from, custom iterators
├── 04-async-concurrency/   # Asyncio, Event Loop, task scheduling
├── 05-web-frameworks/      # Flask contexts, FastAPI DI, Pydantic
└── 06-building-challenges/ # Decorator, router, custom Future
```

## Running Puzzles

```bash
# Run a specific puzzle
uv run python 01-core-mechanics/puzzle_01_mutable_defaults.py

# Run all puzzles in a module
uv run python -m 01-core-mechanics

# Run tests (if any)
uv run pytest
```

## Development

```bash
# Install dependencies
uv sync --all-extras

# Run linter
uv run ruff check .

# Fix linting issues
uv run ruff check . --fix
```

## Topics Covered

### Module 1: Core Mechanics
- Mutable default arguments
- Closure late binding
- LEGB scope (Local, Enclosing, Global, Built-in)

### Module 2: OOP Internals
- Method Resolution Order (MRO)
- Class vs instance variables
- `__new__` vs `__init__`

### Module 3: Generators & Iterators
- `yield` basics
- `yield from` delegation
- Custom iterators

### Module 4: Async & Concurrency
- Blocking the event loop
- Task scheduling with `create_task`
- Async context managers

### Module 5: Web Frameworks
- Flask request context
- FastAPI dependency injection
- Pydantic validation

### Module 6: Building Challenges
- `@retry` decorator
- Simple WSGI router
- Custom Future/Promise implementation
