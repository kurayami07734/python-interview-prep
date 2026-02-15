# QUESTION: What is the output of this code and why?

import asyncio


class AsyncDBConnection:
    def __init__(self, name):
        self.name = name
        self.connected = False

    async def __aenter__(self):
        print(f"[{self.name}] Connecting...")
        await asyncio.sleep(0.1)
        self.connected = True
        print(f"[{self.name}] Connected!")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"[{self.name}] Disconnecting...")
        await asyncio.sleep(0.1)
        self.connected = False
        print(f"[{self.name}] Disconnected!")
        return False

    async def query(self, sql):
        print(f"[{self.name}] Executing: {sql}")
        await asyncio.sleep(0.1)
        return f"Result for: {sql}"


async def main():
    print("=== Using async context manager ===")
    async with AsyncDBConnection("DB1") as conn:
        result = await conn.query("SELECT * FROM users")
        print(f"Query result: {result}")
        print(f"Connected: {conn.connected}")

    print(f"After context: Connected = {conn.connected}")


asyncio.run(main())
