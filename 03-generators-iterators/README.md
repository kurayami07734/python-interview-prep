# Generators & Iterators

This module explores Python's generator and iterator protocols—the mechanisms that power lazy evaluation and memory-efficient processing.

## Topics Covered

### Yield
The `yield` keyword turns a function into a generator. Unlike regular functions that run to completion, generators produce values lazily and maintain their state between calls. Each `yield` pauses execution and remembers local variables.

### Yield From
`yield from` delegates to subgenerators, creating a bidirectional channel for values and exceptions. It's the foundation for building coroutines and simplifies generator pipelines.

### Custom Iterators
Implementing `__iter__` and `__next__` allows any class to participate in iteration. The iterator protocol is what `for` loops use internally.

## Running the Puzzles

```bash
uv run python 03-generators-iterators/puzzle_01_yield_basics.py
uv run python 03-generators-iterators/puzzle_02_yield_from.py
uv run python 03-generators-iterators/puzzle_03_custom_iterators.py
```
