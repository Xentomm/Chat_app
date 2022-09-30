from multiprocessing.connection import Listener
import socket
import threading
from urllib import response

HOST = "127.0.0.1"
PORT = 1234
LISTNER_LIMIT = 5

# List of connected users
active_clients = []

def listen_for_messages(client, username):
    while 1:
        message = client.recv(2048).decode('utf-8')
        if message != '':
            final_msg = username + ': ' + message
            send_messages_to_all(final_msg)
        else:
            print(f"Nie można wysłać pustej wiadomości od {username}")

# Function to send msg to single connected client
def send_message_to_client(client, message):
    client.sendall(message.encode())

# Function to send msg to all connected clients
def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message)

# Function to handle client
def client_handler(client):
    # Server will listen for client msg
    while 1:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
            prompt_message = "SERVER: " + f"{username} został dodany do chatu"
            send_messages_to_all(prompt_message)
            break
        else:
            print("Nazwa urzytkownika jest pusta")
    
    threading.Thread(target = listen_for_messages, args = (client, username, )).start()

def main():
    # AD_INET, IPv4
    # SOCK_STREAM, TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((HOST, PORT))
        print(f"Połączono serwer na {HOST} {PORT}")
    except:
        print(f"Nieudane połączenie {HOST} z portem {PORT}")

    # Server limit
    server.listen(LISTNER_LIMIT)

    while 1:
        client, adress = server.accept()
        print(f"Pomyślnie połączono z klientem {adress[0]} {adress[1]}")

        threading.Thread(target = client_handler, args = (client, )).start()

if __name__ == '__main__':
    main()