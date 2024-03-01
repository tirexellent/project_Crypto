import codecs
import socket

hostname=socket.gethostname()
HOST=socket.gethostbyname(hostname)
PORT = 65432

SERVER_HOST = "vlbelintrocrypto.hevs.ch"
SERVER_PORT = 6000


# returns length in 2 bytes
def get_message_length(length):
    res = bytearray()
    res.extend(str(length).encode().rjust(2, b'\x00')) # .to_bytes(2, byteorder='big')
    print(f'message length of {length} is {res}')
    return res


# returns message as 4 bytes per character
def get_message_characters(message):
    res = bytearray()
    if isinstance(message, str):
        for c in message:
            res.extend(c.encode().rjust(4, b'\x00'))
    return res


def create_message(m, t):
    data = []
    if isinstance(m, str):        
        data = b"ISC"
        data += t.encode()

        if t == 't':
            length = len(m)
            # 2 bytes for length
            data += get_message_length(length)
            # 4 bytes per character in message
            data += get_message_characters(m)
        elif t == 'i':
            print("image")
        elif t == 's':
            print("server")

        print(f"Sent data: {data}")

    return data

# OPENING LISTENING PORT
# AF_INET = IPv4, SOCK_STREAM = TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_HOST, SERVER_PORT))

    message = "test"
    type = "t"

    data = create_message(message, type)

    s.sendall(data)
    rcv = s.recv(1024)
    
print(f"Received {rcv.decode()}")