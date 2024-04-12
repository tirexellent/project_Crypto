from message import Message
from algorithm import Algorithm
from shift import Shift
from vigenere import Vigenere
import socket

SERVER_HOST = "vlbelintrocrypto.hevs.ch"
SERVER_PORT = 6000    

# OPENING LISTENING PORT
# AF_INET = IPv4, SOCK_STREAM = TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_HOST, SERVER_PORT))
    s.setblocking(False)

    alg = "vigenere"
    task = "encode"
    size = 8

    m = f"task {alg} {task} {size}"
    t = "s"

    msg = Message(t, m)
    s.sendall(msg.data)

    num_bytes = 4
    state = 1

    algo: Algorithm = Vigenere()
    algo.task = task
    
    while(True):
        try:
            # read ISC + type   
            if state == 1:
                rcv = s.recv(4)
                print(f"rcv {state} {rcv}")

            # read msg length
            if state == 2:
                rcv = s.recv(2)
                algo.info_msg_size = int.from_bytes(rcv)
                print(f"rcv {state} {rcv}")

            # read info with key
            if state == 3:
                rcv = s.recv(algo.info_msg_size*4)
                print(f"rcv {state} {rcv.decode()}")

                algo.getKey(rcv.decode())

            # read msg to encode/decode
            if state == 4:
                rcv = s.recv(6 + size*4)
                print(f"rcv {state} {rcv.decode()}")

                if task == "encode":
                    if algo.message == "":
                        algo.message = rcv.decode()[6:] # substring 6 to end
                    m = Message('s', algo.encode_message())
                elif task == "decode":
                    if algo.encoded_message == bytearray():
                        msg: str = rcv.decode()[6:]
                        
                        algo.encoded_message.extend(map(ord, msg)) # substring 6 to end
                    m = Message('s', algo.decode_message())
                
            
            if state == 5:
                if algo.task == "decode":
                    s.sendall(m.data)
                # rcv = s.recv(6 + size*4)
                # print(f"rcv {state} {rcv}")

            state += 1
        except Exception as err:
            # pass
            if type(err) != BlockingIOError:
                print(f"Unexpected {err=}, {type(err)=}")
        else:
            pass
            # print(f"Received {rcv.decode()}")
