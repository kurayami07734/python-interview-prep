# Building Challenges

This module contains hands-on implementations of core Python patterns.

## Challenges

### 1. Retry Decorator (`challenge_01_retry_decorator.py`)

**Implementation:** A decorator that retries a function on failure.

```python
def retry(times=3, delay=0.1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < times - 1:
                        time.sleep(delay)
            raise e
        return wrapper
    return decorator
```

**Key Concepts:**
- Function decorators with arguments (factory pattern)
- `functools.wraps` preserves function metadata
- Exception handling and retry logic

**References:**
- [Python Docs - functools](https://docs.python.org/3/library/functools.html)
- [PEP 318 - Decorators](https://peps.python.org/pep-0318/)

---

### 2. Simple Router (`challenge_02_simple_router.py`)

**Implementation:** A WSGI-compatible router.

```python
class App:
    def __init__(self):
        self.routes = {}
    
    def route(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator
    
    def __call__(self, environ, start_response):
        # WSGI interface
        ...
```

**Key Concepts:**
- WSGI (Web Server Gateway Interface)
- Decorator pattern for route registration
- Callable classes

**References:**
- [PEP 333 - Python Web Server Gateway Interface](https://peps.python.org/pep-0333/)
- [Python Docs - wsgiref](https://docs.python.org/3/library/wsgiref.html)

---

### 3. Custom Future (`challenge_03_custom_future.py`)

**Implementation:** A Promise/Future implementation with callbacks.

```python
class Future:
    def __init__(self):
        self._result = None
        self._exception = None
        self._done = False
        self._callbacks = []
    
    def add_done_callback(self, fn):
        if self._done:
            fn(self)
        else:
            self._callbacks.append(fn)
    
    def set_result(self, result):
        self._done = True
        for cb in self._callbacks:
            cb(self)
```

**Key Concepts:**
- Callback pattern
- Thread-safe state management with locks
- Futures/Promises for async programming

**References:**
- [asyncio.Future Documentation](https://docs.python.org/3/library/asyncio-future.html)
- [PEP 3148 - Futures for Concurrent Computation](https://peps.python.org/pep-3148/)
