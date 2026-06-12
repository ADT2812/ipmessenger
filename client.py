import socket
import threading

PORT = 5000

target_ip = input("Enter Receiver IP: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((target_ip, PORT))
    print("Connected!")

except Exception as e:
    print("Connection failed:", e)
    exit()


def receive_messages():

    while True:

        try:

            message = client.recv(1024).decode()

            print(f"\nFriend: {message}")

        except Exception as e:

            print("\nConnection lost.")
            break


receive_thread = threading.Thread(target=receive_messages, daemon=True)

receive_thread.start()


while True:

    message = input("You: ")

    try:
        client.send(message.encode())

    except Exception as e:
        print("Failed to send message.")
        break