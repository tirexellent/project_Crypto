from message import Message

class Vigenere():
    def __init__(self, m: str = "", k: str = ""):
        self.message = m
        self.key = k

    def start_encoding(self, s, t):
        self.getKey(s.receive_str(t))
        msg = s.receive_str(t)        
        encoded = self.encode_message(msg)
        s.send_bytes(t, encoded)

        s.receive_str(t)

    def start_decoding(self, s, t):
        pass

    def encode_message(self, msg) -> bytearray:
        res = bytearray()
        alph: str = "abcdefghijklmnopqrstuvwxyz"
        
        if isinstance(msg, str):
            key: str = self.key.lower()
            while len(key) < len(msg):
                key += self.key.lower()
            
            key_index = 1
            for c in Message.message_to_4_bytes_array(msg):
                print(c)

                # c = msg[i-1].lower()

                # shift = 0
                # current_key = key[key_index*4-1]
                # if current_key in alph:
                #     shift = alph.index(current_key.lower())
                # else:
                #     shift = int.from_bytes(current_key.encode())
                    
                # byte: bytes = (int.from_bytes(c.encode()) + shift).to_bytes()
                # print(f"{c} shifted by {shift} is {byte.decode()}")
                # res.extend(byte)

                # if i % 4 == 0:
                #     key_index += 1

        return res

    def decode_message(self) -> bytearray:
        pass
    
    def getKey(self, rcv) -> None:
        if self.key == "":
            self.key = str(rcv.split()[-1])
