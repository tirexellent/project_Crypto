from server_socket import Socket

import server
import public
SERVER_HOST = "vlbelintrocrypto.hevs.ch"
SERVER_PORT = 6000    

s = Socket()
s.connect(SERVER_HOST, SERVER_PORT)

while True:
    print("_______________________________")
    print("Server or public ? [s/p]")
    t = input()
    
    match t:
        case "s":
            server.chat(s)
        case "p":
            public.chat(s)