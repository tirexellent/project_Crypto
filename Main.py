import socket

hostname=socket.gethostname()
HOST=socket.gethostbyname(hostname)
PORT = 65432

SERVER_HOST = "vlbelintrocrypto.hevs.ch"
SERVER_PORT = 6000



# OPENING LISTENING PORT
# AF_INET = IPv4, SOCK_STREAM = TCP

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()

#     conn, addr = s.accept()
#     with conn:
#         print(f"Connected by {addr}")
#         while (true):
#             data = conn.recv(1024)
#             if not data:
#                 break
#             print(f"Data recieved: {data}")


def create_message(m):
    data = []
    if isinstance(m, str):
        length = len(m)
        
        data = b"ISCt"
        data += str(length).encode()

        for i in range(length):
            data += m[i].encode()
        
        print(data)

    return data

# CLIENT
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_HOST, SERVER_PORT))

    message = "g"

    data = create_message(message)

    s.sendall(data)
    rcv = s.recv(1024)
    
print(f"Received {data!r}")