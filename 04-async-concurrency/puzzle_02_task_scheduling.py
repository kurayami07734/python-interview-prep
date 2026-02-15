# QUESTION: What is the output of this code and why?

import asyncio


async def coro(name, delay):
    await asyncio.sleep(delay)
    return f"{name} done"


async def main():
    print("=== create_task (fire and forget) ===")
    task1 = asyncio.create_task(coro("A", 0.5))
    task2 = asyncio.create_task(coro("B", 0.1))
    task3 = asyncio.create_task(coro("C", 0.3))

    print("Tasks created, awaiting results...")
    results = await asyncio.gather(task1, task2, task3)
    print(f"Results: {results}")

    print("\n=== Direct await (sequential) ===")
    r1 = await coro("D", 0.5)
    r2 = await coro("E", 0.1)
    r3 = await coro("F", 0.3)
    print(f"Results: [{r1}, {r2}, {r3}]")


asyncio.run(main())
