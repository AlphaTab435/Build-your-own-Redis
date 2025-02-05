import asyncio

async def start_client():
    reader, writer = await asyncio.open_connection("localhost", 6379)

    messages = ["Hello Server!", "How are you?", "exit"]
    # messages = ["Hello Server!"]

    for msg in messages:
        writer.write(msg.encode())
        await writer.drain()  # Ensure message is sent

        response = await reader.read(1024)
        print(f"Server Response: {response.decode()}")

        await asyncio.sleep(1)  # Simulating delay between messages

    writer.close()
    await writer.wait_closed()

if __name__ == "__main__":
    asyncio.run(start_client())
    asyncio.run(start_client())
    asyncio.run(start_client())


# Async TCP Client (Sends Messages Without Blocking)
'''
How It Works
await asyncio.open_connection("localhost", 6379) → Connects asynchronously.
writer.write(msg.encode()) → Sends data without blocking.
await writer.drain() → Ensures the data is sent before proceeding.
await reader.read(1024) → Reads server response without blocking.
await asyncio.sleep(1) → Simulates delay between messages.
'''