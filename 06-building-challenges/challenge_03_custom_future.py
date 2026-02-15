# Build a custom Promise/Future class that mimics asyncio.Future with callbacks.

from typing import Any, Callable, List, Optional
import threading


class Future:
    def __init__(self):
        self._result: Optional[Any] = None
        self._exception: Optional[Exception] = None
        self._done: bool = False
        self._callbacks: List[Callable] = []
        self._lock = threading.Lock()

    def result(self) -> Any:
        if self._exception:
            raise self._exception
        return self._result

    def exception(self) -> Optional[Exception]:
        return self._exception

    def done(self) -> bool:
        return self._done

    def add_done_callback(self, fn: Callable) -> None:
        with self._lock:
            if self._done:
                fn(self)
            else:
                self._callbacks.append(fn)

    def set_result(self, result: Any) -> None:
        with self._lock:
            if self._done:
                raise RuntimeError("Future already done")
            self._result = result
            self._done = True
            callbacks = self._callbacks.copy()
        for cb in callbacks:
            cb(self)

    def set_exception(self, exception: Exception) -> None:
        with self._lock:
            if self._done:
                raise RuntimeError("Future already done")
            self._exception = exception
            self._done = True
            callbacks = self._callbacks.copy()
        for cb in callbacks:
            cb(self)


def executor(future: Future, fn: Callable, *args, **kwargs):
    try:
        result = fn(*args, **kwargs)
        future.set_result(result)
    except Exception as e:
        future.set_exception(e)


def submit(fn: Callable, *args, **kwargs) -> Future:
    future = Future()
    thread = threading.Thread(target=executor, args=(future, fn) + args, kwargs=kwargs)
    thread.start()
    return future


print("=== Testing custom Future ===")

def slow_add(a, b):
    import time
    time.sleep(0.5)
    return a + b


print("Submitting task...")
future = submit(slow_add, 10, 20)

print(f"Done immediately? {future.done()}")
print("Waiting for result...")

while not future.done():
    import time
    time.sleep(0.1)

print(f"Result: {future.result()}")

print("\n=== Testing callbacks ===")
future2 = submit(slow_add, 5, 15)


def callback(f):
    print(f"Callback triggered! Result: {f.result()}")


future2.add_done_callback(callback)

while not future2.done():
    import time
    time.sleep(0.1)

print("\n=== Testing exception handling ===")


def failing_task():
    raise ValueError("Intentional error!")


future3 = submit(failing_task)

while not future3.done():
    import time
    time.sleep(0.1)

try:
    future3.result()
except ValueError as e:
    print(f"Caught exception: {e}")
