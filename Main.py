from message import Message
from cipher import Cipher
from shift import Shift
from vigenere import Vigenere
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

    alg = "vigenere"
    size = 6

    m = f"task {alg} encode {size}"
    t = "s"

    msg = Message(t, m)
    s.sendall(msg.data)

    num_bytes = 4
    state = 1

    # _cipher = Shift(msg, 4)
    # print(_cipher.encode_message().decode())
    # print(_cipher.decode_message().decode())

    # _cipher: Cipher = Vigenere(msg, "abcd")
    # print(_cipher.encode_message().decode())
    # print(_cipher.decode_message().decode())
    
    
    #TODO: Make dynamic with different cipher algosrithms
    # Loop for shift
    # while(True):
    #     try:
    #         if state == 1:
    #             rcv = s.recv(4)
    #             print(f"rcv 1 {rcv}")
    #             state += 1
    #         if state == 2:
    #             rcv = s.recv(2)
    #             print(f"rcv 2 {rcv}")
    #             msg_size = int.from_bytes(rcv)
    #             state += 1
    #         if state == 3:
    #             rcv = s.recv(msg_size*4)
    #             print(f"rcv 3 {rcv.decode()}")
    #             state += 1
    #         if state == 4:
    #             rcv = s.recv(6 + size*4)
    #             print(f"rcv 4 {rcv.decode()}")

    #     except:
    #         pass
    #     else:
    #         pass
    #         # print(f"Received {rcv.decode()}")

    # Loop for vigenere
    while(True):
        try:
            # read ISC + type
            if state == 1:
                rcv = s.recv(4)
                print(f"rcv 1 {rcv}")
                state += 1
            # read msg length
            if state == 2:
                rcv = s.recv(2)
                print(f"rcv 2 {rcv}")
                msg_size = int.from_bytes(rcv)
                state += 1
            # read msg and key
            if state == 3:
                rcv = s.recv(msg_size*4)
                res = rcv.decode()
                print(f"rcv 3 {res}")
                key = res.split()[-1]
                state += 1
            # read msg base to encrypt
            if state == 4:
                rcv = s.recv(6)
                print(f"rcv 4 {rcv.decode()}")
                state += 1
            # read msg to encode
            if state == 5:
                rcv = s.recv(size*4)
                print(f"rcv 5 {rcv.decode()}")
                _vigenere = Vigenere(Message("s", rcv.decode()), key)
                print("Encoded: ", _vigenere.encode_message().decode())
                break
        except:
            pass
        else:
            pass
            # print(f"Received {rcv.decode()}")
