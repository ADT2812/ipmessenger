import socket
import threading

PORT = 5000

target_ip = input("Enter Receiver IP: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_ip, PORT))

print("Connected!")


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