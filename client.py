import socket
import threading

HOST = '192.168.248.162'  # server host
PORT = 8090  # server port

CHARACTERS = ["All","Rocco","Eva","Lele","Carlotta","Peppe","Bianca","Cosimo"]
EMOTIONS = {"B":"happy","E": "angry","D": "shocked","E": "sad","F": "relaxed", "G": "afraid","H": "cautious","I": "surprised","J": "annoyed","K": "embarrassed","L": "anxious"}

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the server's address and port
sock.connect((HOST, PORT))

def receive_messages():
    """Thread function to receive messages from the server"""
    while True:
        try:
            data = sock.recv(1024).decode()
            if data[0] == "G":
                print(f"God sent SMS: {data}")
            elif len(data)==5:
                print(f"{ CHARACTERS[int(data[0])]} is {EMOTIONS[data[1]]}({data[3]}) with {CHARACTERS[int(data[2])]}")
            else:
                print(f"{data}")
        except Exception as e:
            print(f"Error: {e}")
            break

def send_messages():
    """Thread function to send messages to the server"""
    while True:
        try:
            data = input("> ") + "\n"
            sock.send(data.encode())
        except Exception as e:
            print(f"Error: {e}")
            break

# start threads to receive and send messages
threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()
