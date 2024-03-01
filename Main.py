from message import Message
from shift import Shift
import socket

hostname=socket.gethostname()
HOST=socket.gethostbyname(hostname)
PORT = 65432

SERVER_HOST = "vlbelintrocrypto.hevs.ch"
SERVER_PORT = 6000


def foo(rcv, num_bytes):
    if num_bytes == 4:
        return 2
    if num_bytes == 2:
        return 79
    

# OPENING LISTENING PORT
# AF_INET = IPv4, SOCK_STREAM = TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_HOST, SERVER_PORT))
    s.setblocking(False)
    m = "task shift encode 6"
    t = "s"

    msg = Message(t, m)
    # s.sendall(msg.data)

    num_bytes = 4
    state = 1

    print(m)
    _shift = Shift(msg, 2)
    print(_shift.encode_message().decode())
    print(_shift.decode_message().decode())
    
    # while(True):
    #     try:
    #         if state == 1:
    #             rcv = s.recv(4)
    #             state += 1
    #         if state == 2:
    #             rcv = s.recv(2)
    #             print(f"rcv {rcv}")
    #             msg_size = int.from_bytes(rcv)
    #             state += 1
    #         if state == 3:
    #             rcv = s.recv(msg_size*4)
    #             state += 1
    #         if state == 4:
    #             rcv = s.recv(6)

    #     except:
    #         pass
    #     else:
    #         print(f"Received {rcv.decode()}")
