'''
Key Functions in the socket Module:
socket.socket(): Creates a new socket.

bind(): Binds the socket to a specific address and port.

listen(): Puts the socket in listening mode (for servers).

accept(): Accepts an incoming connection (for servers).

connect(): Connects to a remote socket (for clients).

send(): Sends data through the socket.

recv(): Receives data from the socket.

close(): Closes the socket.
'''

import socket  # noqa: F401
import platform

def checkIfWindows():
    system = platform.system()
    if system == "Windows":
        return True
    return False


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    isWindows=checkIfWindows()
    if(isWindows):
        server_socket = socket.create_server(("localhost", 6379))
        print("Server started on port 6379")

        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allows address reuse
    else:
        server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    
    client_conn, client_addr =server_socket.accept() # wait for client
    client_conn.sendall("PONG".encode())


if __name__ == "__main__":
    main()
