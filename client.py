import socket
import threading

HOST = '192.168.1.25'  # server host
PORT = 8090  # server port

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the server's address and port
sock.connect((HOST, PORT))

def receive_messages():
    """Thread function to receive messages from the server"""
    while True:
        try:
            data = sock.recv(1024).decode()
            print(data)
        except Exception as e:
            print(f"Error: {e}")
            break

def send_messages():
    """Thread function to send messages to the server"""
    while True:
        try:
            data = input("> ")
            sock.send(data.encode())
        except Exception as e:
            print(f"Error: {e}")
            break

# start threads to receive and send messages
threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
