class Message():
    def __init__(self, t, b) -> None:
        self.type = t
        self.body = b
        self.data = self.create_message(t,b)

    # returns length in 2 bytes
    def get_message_length(self, length):
        return length.to_bytes(2, byteorder='big')
        
    # returns message as 4 bytes per character
    def get_message_characters(self, message):
        res = bytearray()
        if isinstance(message, str):
            for c in message:
                res.extend(c.encode().rjust(4, b'\x00'))
        return res


    def create_message(self, t, m):
        data = []
        if isinstance(m, str):        
            data = b"ISC"
            data += t.encode()

            if t == 't':
                length = len(m)
                self.length = length
                # 2 bytes for length
                data += self.get_message_length(length)
                # 4 bytes per character in message
                data += self.get_message_characters(m)
            elif t == 'i':
                print("image")
            elif t == 's':
                print("server")

            print(f"Sent data: {data}")

        self.data = data
        return data