import socket

def start_server():
    server_socket = socket.create_server(("localhost", 6379))
    # server_socket = socket.create_server(("localhost", 6379), reuse_port=True)

    print("Server is listening on port 6379...")

    while True:
        client_conn, client_addr = server_socket.accept()  # Accept a connection
        print(f"Connected by {client_addr}")
        print(f"Client Connection {client_conn}")

        # Receive data from the client
        data = client_conn.recv(1024).decode()
        if data:
            print(f"Received from client: {data}")
            client_conn.sendall(f"Echo: {data}".encode())  # Echo response

        client_conn.close()  # Close client connection

if __name__ == "__main__":
    start_server()
