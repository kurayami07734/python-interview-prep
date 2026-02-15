# QUESTION: What is the output of this code and why?

import asyncio
import time


async def blocking_task(n):
    print(f"Task {n} starting (blocking)")
    time.sleep(1)
    print(f"Task {n} finished")
    return n


async def non_blocking_task(n):
    print(f"Task {n} starting (non-blocking)")
    await asyncio.sleep(1)
    print(f"Task {n} finished")
    return n


async def main_blocking():
    start = time.time()
    results = await asyncio.gather(*[blocking_task(i) for i in range(3)])
    print(f"Blocking total time: {time.time() - start:.2f}s")
    return results


async def main_non_blocking():
    start = time.time()
    results = await asyncio.gather(*[non_blocking_task(i) for i in range(3)])
    print(f"Non-blocking total time: {time.time() - start:.2f}s")
    return results


print("=== Blocking tasks ===")
asyncio.run(main_blocking())

print("\n=== Non-blocking tasks ===")
asyncio.run(main_non_blocking())
