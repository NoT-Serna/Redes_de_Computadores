import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))

def send_msg():
    print("Connected to the server. Type messages to send.")
    while True:
        message = input("You: ")
        client.send(message.encode('utf-8'))

def receive_msg():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg:
                print(msg)
        except:
            print("An error occurred. Disconnecting from server.")
            client.close()
            break

if __name__ == "__main__":
    threading.Thread(target=receive_msg, daemon=True).start()
    send_msg()
