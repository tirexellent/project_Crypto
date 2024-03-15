from message import Message
from algorithm import Algorithm
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

    _algorithm: Algorithm = Vigenere()
    # print(_cipher.encode_message().decode())
    # print(_cipher.decode_message().decode())

    # _cipher: Cipher = Vigenere(msg, "abcd")
    # print(_cipher.encode_message().decode())
    # print(_cipher.decode_message().decode())
    
    
    #TODO: Make dynamic with different cipher algorithms
    while(True):
        try:
            _algorithm.run_state(state, s, size)
            state += 1
        except Exception as err:
            pass
            # print(f"Unexpected {err=}, {type(err)=}")
            # break
        else:
            pass
            # print(f"Received {rcv.decode()}")
