import socket
import conversion

class Socket():
    # OPENING LISTENING PORT
    # AF_INET = IPv4, SOCK_STREAM = TCP
    def __init__(self) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setblocking(True)
        self.__abortingReceived = False

    def connect(self, host, port):
        self.host = host
        self.port = port
        self.s.connect((host, port))

    def reconnect(self):
        self.__abortingReceived = True
        try:
            self.s.close()
        except socket.error as e:
            pass
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect(self.host, self.port)



    def send_str(self, t: str, msg: str):        
        data = b"ISC"
        data += t.encode()
        
        data += len(msg).to_bytes(2, byteorder='big')

        data += self.get_message_characters(msg)

        print("Sending: ", data.decode())
        self.s.send(data)

    def get_message_characters(self, message: str) -> bytearray:
        res = bytearray()
        if isinstance(message, str):
            for c in message:
                res.extend(c.encode().rjust(4, b'\x00'))
        return res
    
    def send_bytes(self, t: str, msg: bytes):
        data = b"ISC"
        data += t.encode()
        
        data += (len(msg)//4).to_bytes(2, byteorder='big')

        data += msg

        # print("Sending: ", data.decode())
        self.s.send(data)
    
    def receive_bytes(self, t: str):
        while True:
            try:
                rcv = b''
                while len(rcv) == 0 and rcv[0:3].decode("utf-8") != "ISC" and rcv[3:4] != t:
                    rcv = self.s.recv(6)
                

                length = int.from_bytes(rcv[4:6])

                content = self.s.recv(length*4)
                while len(content) < length * 4:
                    content += self.s.recv(length*4 - len(content))
                
                return content
            except Exception as err:
                raise err

    def receive_str(self, t: str):
        while True:
            try:
                rcv = b''
                while len(rcv) == 0 and rcv[0:3].decode("utf-8") != "ISC" and rcv[3:4] != t:
                    rcv = self.s.recv(6)
                
                # print(f"rcv {rcv}")

                length = int.from_bytes(rcv[4:6])

                content = self.s.recv(length*4)
                while len(content) < length * 4:
                    content += self.s.recv(length*4 - len(content))
                
                arr = []
                for i in range(0,length*4,4):
                    try:
                        arr.append(int.from_bytes(content[i:i+4],"big"))
                    except:
                        pass
                
                message_str = conversion.intarray_to_str(arr)
                print(message_str)
                return message_str
            
            except Exception as err:
                raise err
            else:
                pass