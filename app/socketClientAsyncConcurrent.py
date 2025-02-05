import asyncio

async def start_client(client_id):
    reader, writer = await asyncio.open_connection("localhost", 6379)

    messages = ["PING", "Hello Server!", "exit"]

    for msg in messages:
        print(f"Client {client_id} sending: {msg}")
        writer.write(msg.encode() + b"\r\n")  # Ensures Redis-style newline
        await writer.drain()

        response = await reader.read(1024)
        print(f"Client {client_id} received: {response.decode().strip()}")

        await asyncio.sleep(1)  # Simulate delay

    writer.close()
    await writer.wait_closed()

async def main():
    clients = [start_client(i) for i in range(3)]  # 3 clients running concurrently
    await asyncio.gather(*clients)  # Run all clients together

if __name__ == "__main__":
    asyncio.run(main())
