import asyncio

async def handleClient(reader, writer):
     addr = writer.get_extra_info("peername")
     print(f"Connected to {addr}")
     '''
     If multiple clients need to send multiple requests, your server must handle persistent connections instead of closing the connection immediately after the first request.
     Key Changes to Support Multiple Requests Per Client:
     Keep the connection open until the client disconnects.
     Use a loop inside handle_client() to keep reading and responding.
     Break the loop if the client sends an empty request (disconnects).
     '''
    #  data = await reader.read(100)  # Read client request
     while True:
        data = await reader.read(1024)  # Non-blocking read
        if not data:
            print(f"Client {addr} disconnected")
            break
        message = data.decode()
        print(f"Received from {addr}: {message}")
        writer.write(b"+PONG\r\n")  # Send PONG response
        await writer.drain()
     writer.close()
     await writer.wait_closed()
     print(f"Connection with {addr} closed.")



async def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")
    server_socket= await asyncio.start_server(handleClient ,"localhost",6379)
    # print("Server started on port 6379")
    addr = server_socket.sockets[0].getsockname()
    print(f"Server started on {addr}")
    async with server_socket:
         await server_socket.serve_forever() # Keep running


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\nServer shutting down...")
