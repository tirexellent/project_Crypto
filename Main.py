from message import Message
import socket

hostname=socket.gethostname()
HOST=socket.gethostbyname(hostname)
PORT = 65432

SERVER_HOST = "vlbelintrocrypto.hevs.ch"
SERVER_PORT = 6000

# OPENING LISTENING PORT
# AF_INET = IPv4, SOCK_STREAM = TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_HOST, SERVER_PORT))
    s.setblocking(False)
    m = "Se7en ahaha"
    t = "t"

    msg = Message(t, m)
    s.sendall(msg.data)

    recieved = False
    
    while(not recieved):
        try:
            rcv = s.recv(len(msg.data))
        except:
            pass
        else:
            recieved = True
            print(f"Received {rcv.decode()}")
    