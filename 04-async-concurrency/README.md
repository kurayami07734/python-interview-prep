# Async & Concurrency

This module explores asyncio, the event loop, and concurrency in Python—essential knowledge for building high-performance I/O-bound applications.

## Topics Covered

### Event Loop
The heart of asyncio. Understanding blocking vs non-blocking operations is critical: `time.sleep()` blocks the entire thread, while `asyncio.sleep()` yields control back to the event loop, allowing other tasks to run.

### Task Scheduling
`asyncio.create_task()` schedules coroutines to run concurrently (fire-and-forget), while `await` runs them sequentially. Choosing between them affects performance dramatically.

### Async Context Managers
Implementing `__aenter__` and `__aexit__` as async methods enables resource management with `async with`. Essential for database connections, HTTP sessions, and any async resource lifecycle.

## Running the Puzzles

```bash
uv run python 04-async-concurrency/puzzle_01_blocking_loop.py
uv run python 04-async-concurrency/puzzle_02_task_scheduling.py
uv run python 04-async-concurrency/puzzle_03_async_context_manager.py
```
