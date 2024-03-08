class Shift:
    def __init__(self, m, k):
        self.message = m
        self.key = k

    def encode_message(self):        
        res = bytearray()
        if isinstance(self.message.body, str):
            for c in self.message.body:
                byte = (int.from_bytes(c.encode()) + self.key).to_bytes(4, byteorder="big")
                res.extend(byte.rjust(4, b'\x00'))
        self.encoded_message = res
        return res
    
    def decode_message(self):        
        res = bytearray()
        if isinstance(self.message.body, str):
            print(self.encoded_message.decode())
            for c in self.encoded_message.decode():
                code = int.from_bytes(c.encode()) - self.key # utf-8 char value
                if code >= 0:
                    byte = code.to_bytes(4, byteorder="big")
                    res.extend(byte.rjust(4, b'\x00'))
        return res