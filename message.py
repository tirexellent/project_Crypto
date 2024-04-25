class Message:
    def __init__(self, t: str, b: str | bytearray, length: int = 0) -> None:
        self.type = t
        self.body = b
        self.length = length
        self.data = self.create_message(t,b)

    # returns length in 2 bytes
    def get_message_length(self, length: int) -> bytes:
        return length.to_bytes(2, byteorder='big')
        
    # returns message as 4 bytes per character
    def get_message_characters(self, message: str) -> bytearray:
        res = bytearray()
        if isinstance(message, str):
            for c in message:
                res.extend(c.encode().rjust(4, b'\x00'))
        return res


    def create_message(self, t: str, m: str | bytearray) -> str:  
        self.data = b"ISC"
        self.data += t.encode()

        # if message is already encoded
        if type(m) == bytearray or type(m) == bytes:
            # 2 bytes for length
            self.data += self.get_message_length(self.length)
            self.data += m

        elif type(m) == str:
            self.length = len(m)
            # 2 bytes for length
            self.data += self.get_message_length(self.length)
            # 4 bytes per character in message
            self.data += self.get_message_characters(m)

        return self.data
        
    
    @staticmethod
    def bytes_to_string(x: str):
        # every 4 bytes is one char
        res = ""
        chars: list[bytearray] = []
        c = bytearray()
        i = 0

        for b in x:
            try:
                b = int(b)
                c.extend(b.to_bytes().rjust(1, b'\x00'))
            except ValueError:
                c.extend(b.encode().rjust(1, b'\x00'))

            i += 1
            if i == 4:
                i = 0
                chars.append(c)
                c = bytearray()

        for s in chars:
            y = int.from_bytes(s)
            res += str(y)
            
        return res
    
    
    @staticmethod
    def message_to_4_bytes_array(message):
        return [message[i:i+4] for i in range(0, len(message), 4)]
