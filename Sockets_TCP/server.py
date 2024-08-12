import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen(5)
print("Server started, waiting for connections...")

clients = []
chat = []

def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                msg = f"Client {client_address}: {message}"
                print(msg)
                chat.append(msg)
                for client in clients:
                    if client != client_socket:
                        try:
                            client.sendall(msg.encode('utf-8'))
                        except:
                            clients.remove(client)
        except:
            print(f"Client {client_address} disconnected")
            clients.remove(client_socket)
            client_socket.close()
            break

def main():
    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        print(f"Accepted connection from {addr}")
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()

if __name__ == "__main__":
    main()
