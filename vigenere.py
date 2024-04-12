from algorithm import Algorithm
from message import Message

class Vigenere(Algorithm):
    def __init__(self, m: str = "", k: str = ""):
        self.message = m
        self.key = k

    # TODO: Encode vigenere
    def encode_message(self) -> bytearray:
        res = bytearray()
        alph: str = "abcdefghijklmnopqrstuvwxyz"
        m = self.message
        
        if isinstance(m, str):
            key: str = self.key.lower()
            while len(key) < len(m):
                key += self.key.lower()
            
            print(m, key)
            key_index = 1
            for i in range(1, len(m)+1):
                c = m[i-1].lower()

                shift = 0
                current_key = key[key_index*4-1]
                if current_key in alph:
                    # print(f"{current_key} is letter")
                    shift = alph.index(current_key.lower())
                else:
                    # print(f"{key[current_key]} is not letter")
                    shift = int.from_bytes(current_key.encode())
                    
                # print(f"{c} will be shifted by {shift}")
                byte: bytes = (int.from_bytes(c.encode()) + shift).to_bytes()
                res.extend(byte)

                if i % 4 == 0:
                    key_index += 1


        self.encoded_message = res
        print('res:', res)
        return res

    def decode_message(self) -> bytearray:
        pass
    
    def getKey(self, rcv) -> int | str:
        if self.key == "" and self.task == "encode":
            self.key = str(rcv.split()[-1])           
