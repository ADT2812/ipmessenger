import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen(1)

print("Waiting for connection...")

client, address = server.accept()

print(f"Connected to {address[0]}")


def receive_messages():

    while True:

        try:

            message = client.recv(1024).decode()

            print(f"\nFriend: {message}")

        except:

            break


receive_thread = threading.Thread(target=receive_messages, daemon=True)

receive_thread.start()


while True:

    message = input("You: ")

    client.send(message.encode())