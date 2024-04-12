from algorithm import Algorithm
from message import Message

class Shift(Algorithm):
    def __init__(self, m: str = "", k: int = 0):
        self.message: str = m
        self.encoded_message = bytearray()
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
        pass  

    def getKey(self, rcv) -> None:
        if self.key == 0 and self.task == "encode":
            self.key = int(rcv[-1])
            
        