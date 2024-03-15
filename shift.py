from algorithm import Algorithm

class Shift(Algorithm):
    def __init__(self, m: str = "", k: int = 0):
        self.message: str = m
        self.key: int = k

    def encode_message(self) -> bytearray:       
        res = bytearray()
        if isinstance(self.message, str):
            for c in self.message:
                byte = (int.from_bytes(c.encode()) + self.key).to_bytes(4, byteorder="big")
                res.extend(byte.rjust(4, b'\x00'))
        self.encoded_message = res
        print(res.decode())
        return res
    
    def decode_message(self) -> bytearray:        
        res = bytearray()
        if isinstance(self.message, str):
            for c in self.encoded_message.decode():
                code = int.from_bytes(c.encode()) - self.key # utf-8 char value
                if code >= 0:
                    byte = code.to_bytes(4, byteorder="big")
                    res.extend(byte.rjust(4, b'\x00'))
        print(res.decode())
        return res
    
    def run_state(self, state, s, msg_size) -> None:
        # read ISC + type   
        if state == 1:
            rcv = s.recv(4)
            print(f"rcv {state} {rcv}")
        # read msg length
        if state == 2:
            rcv = s.recv(2)
            self.info_msg_size = int.from_bytes(rcv)
            print(f"rcv {state} {rcv} with size {self.info_msg_size}")
        # read info with key
        if state == 3:
            rcv = s.recv(self.info_msg_size*4)
            print(f"rcv {state} {rcv.decode()}")
            if self.key == 0:
                self.key = int(rcv.decode()[-1])
                
        # read msg to encrypt
        if state == 4:
            rcv = s.recv(6 + msg_size*4)
            print(f"rcv {state} {rcv.decode()}")

            if self.message == "":  
                self.message = rcv.decode()[6:] # substring 6 to end

            self.encode_message()
            self.decode_message()
        