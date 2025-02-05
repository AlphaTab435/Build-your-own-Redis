import socket

def start_client():
    # socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
    # socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    # socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)  # Unix domain socket

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 6379))  # Connect to server

    message = "Hello Server!"
    message += "Hello Server! how are you fine Thank You"

    client_socket.sendall(message.encode())  # Send message to server

    response = client_socket.recv(1024).decode()  # Receive response
    print(f"Server Response: {response}")

    client_socket.close()  # Close connection

if __name__ == "__main__":
    start_client()
