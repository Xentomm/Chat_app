import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
LISTNER_LIMIT = 5

def main():
    # AD_INET, IPv4
    # SOCK_STREAM, TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(HOST, PORT)
    except:
        print(f"Nieudane połączenie {HOST} z portem {PORT}")

    # Server limit
    server.listen(LISTNER_LIMIT)

    while 1:
        client, adress = server.accept()
        print(f"Pomyślnie połączono z klientem {adress[0]} {adress[1]}")

if __name__ == '__main__':
    main()