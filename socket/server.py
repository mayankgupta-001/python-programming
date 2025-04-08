import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)

    print("Server is listening on port 12345...")
    conn, addr = server_socket.accept()
    print(f"Connected to {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data or data.lower() == "exit":
            print("Client disconnected.")
            break
        print(f"Client: {data}")
        
        message = input("Server: ")
        conn.sendall(message.encode())

    conn.close()
    server_socket.close()

if __name__ == "_main_":
    start_server()