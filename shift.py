class Shift():
    def __init__(self, m: str = "", k: int = 0):
        self.message: str = m
        self.key: int = k

    def start_encoding(self, s, t):
        self.getKey(s.receive_str(t))
        msg = s.receive_str(t)
        encoded = self.encode_message(msg)
        s.send_bytes(t, encoded)

        return s.receive_str(t)

    def start_decoding(self, s, t):
        s.receive_str(t)
        msg = s.receive_str(t)
        for i in range(30):
            decoded = self.decode_message(msg)
            s.send_str(t, str(self.key))
            res: str = s.receive_str(t)
            if "correct" in res:
                return res
            
            self.key += 1

        
    def encode_message(self, msg) -> bytearray:
        encoded = bytearray()
        if isinstance(msg, str):
            for c in msg:
                byte = (int.from_bytes(c.encode()) + self.key).to_bytes(4, byteorder="big")
                encoded.extend(byte.rjust(4, b'\x00'))
        
        return encoded
    
    def decode_message(self, msg) -> bytearray:
        decoded = bytearray()
        if isinstance(msg, str):
            for c in msg:
                code = int.from_bytes(c.encode()) - self.key # utf-8 char value
                if code >= 0:
                    byte = code.to_bytes(4, byteorder="big")
                    decoded.extend(byte.rjust(4, b'\x00'))

        print(self.key, decoded.decode())
        return decoded

    def getKey(self, rcv) -> None:
        if self.key == 0:
            self.key = int(rcv[-1])
            
        