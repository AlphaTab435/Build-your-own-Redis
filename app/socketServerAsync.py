import asyncio

async def handle_client(reader, writer):
    addr = writer.get_extra_info("peername")
    print(f"Connected to {addr}")

    while True:
        data = await reader.read(1024)  # Non-blocking read
        if not data:
            print(f"Client {addr} disconnected")
            break

        message = data.decode()
        print(f"Received from {addr}: {message}")

        response = f"Echo: {message}"
        writer.write(response.encode())  # Non-blocking write
        await writer.drain()  # Ensure the data is sent

    writer.close()
    await writer.wait_closed()

async def start_server():
    server = await asyncio.start_server(handle_client, "localhost", 6379)
    addr = server.sockets[0].getsockname()
    print(f"Server started on {addr}")

    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(start_server())


# Async TCP Server (Handles Multiple Clients)
'''
How It Works
async def handle_client(reader, writer) → Handles each client connection asynchronously.
await reader.read(1024) → Non-blocking read (does not stop the server).
writer.write(data.encode()) → Sends response without blocking.
await writer.drain() → Ensures data is flushed before continuing.
asyncio.start_server(handle_client, "localhost", 6379) → Starts a TCP server on port 6379.
'''