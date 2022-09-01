import socket
import threading

HOST = '127.0.0.1'
PORT = 1234

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Połączenie z serwerem
    try:
        client.connect(HOST, PORT)
        print(f"Połączono z serwerem")
    except:
        print(f"Nieudanie połaczenie z serwerem {HOST} {PORT}")


if __name__ == '__main__':
    main()