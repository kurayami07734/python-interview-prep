# Async & Concurrency - Solutions

## Puzzle 1: Blocking the Event Loop (`puzzle_01_blocking_loop.py`)

**Output:**
```
=== Blocking tasks ===
Task 0 starting (blocking)
Task 0 finished
Task 1 starting (blocking)
Task 1 finished
Task 2 starting (blocking)
Task 2 finished
Blocking total time: 3.00s

=== Non-blocking tasks ===
Task 0 starting (non-blocking)
Task 1 starting (non-blocking)
Task 2 starting (non-blocking)
Task 0 finished
Task 1 finished
Task 2 finished
Non-blocking total time: 1.00s
```

**Explanation:**

`time.sleep()` is a blocking call - it blocks the entire thread, including the event loop. The async tasks run sequentially (3 seconds).

`await asyncio.sleep()` is non-blocking - it yields control to the event loop, allowing other tasks to run. All three tasks run concurrently (1 second).

**Key Takeaway:** Never use blocking calls (`time.sleep`, synchronous I/O) in async code. Use `asyncio` equivalents.

**References:**
- [Python Docs - asyncio](https://docs.python.org/3/library/asyncio.html)
- [PEP 3156 - asyncio](https://peps.python.org/pep-3156/)

---

## Puzzle 2: Task Scheduling (`puzzle_02_task_scheduling.py`)

**Output:**
```
=== create_task (fire and created, awaiting results forget) ===
Tasks...
Task B done
Task C done
Task A done
Results: ['A done', 'B done', 'C done']

=== Direct await (sequential) ===
Task D done
Task E done
Task F done
Results: ['D done', 'E done', 'F done']
```

**Explanation:**

- `asyncio.create_task()` schedules a coroutine to run concurrently
- Direct `await` runs coroutines sequentially

With `create_task()`, all three tasks are scheduled first, then we await their completion. They run concurrently and finish in order of their sleep duration.

With sequential await, each task must complete before the next starts.

**Key Takeaway:** Use `create_task()` for concurrent execution, `await` for sequential.

**References:**
- [Python Docs - Creating Tasks](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task)

---

## Puzzle 3: Async Context Managers (`puzzle_03_async_context_manager.py`)

**Output:**
```
=== Using async context manager ===
[DB1] Connecting...
[DB1] Connected!
[DB1] Executing: SELECT * FROM users
Query result: Result for: SELECT * FROM users
Connected: True
[DB1] Disconnecting...
[DB1] Disconnected!
After context: Connected = False
```

**Explanation:**

Async context managers implement:
- `__aenter__`: async method for entering the context
- `__aexit__`: async method for exiting the context

The `async with` statement ensures cleanup runs even if an exception occurs.

**Key Takeaway:** Use `async with` for resources that need async setup/teardown (database connections, HTTP sessions).

**References:**
- [Python Docs - Async Context Managers](https://docs.python.org/3/reference/datamodel.html#async-context-managers)
