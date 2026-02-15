# Build a @retry(times=3) decorator that retries a function if it raises an exception.

import functools
import time


def retry(times=3, delay=0.1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < times - 1:
                        print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                        time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator


@retry(times=3)
def flaky_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Random failure!")
    return "Success!"


print("=== Testing retry decorator ===")
for i in range(5):
    try:
        result = flaky_function()
        print(f"Run {i+1}: {result}")
    except ValueError as e:
        print(f"Run {i+1}: Failed after 3 attempts - {e}")
