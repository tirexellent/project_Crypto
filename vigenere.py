from cipher import Cipher

class Vigenere(Cipher):
    def __init__(self, m: str, k: str):
        self.message = m
        self.key = k

    def encode_message(self) -> bytearray:
        res = bytearray()
        alph: str = "abcdefghijklmnopqrstuvwxyz"
        m = self.message.body
        
        if isinstance(m, str):
            key: str = self.key.lower()
            while len(key) < len(m):
                key += self.key.lower()
            
            print(m)
            index = 0
            for i in range(len(m)):
                print(i, m[i].encode())
                if m[i].encode() != b'\x00':
                    c = m[i]

                    if c.lower() in alph:
                        print("c is letter")
                        shift = alph.index(key[index].lower())
                        byte = (int.from_bytes(c.encode()) + shift).to_bytes(4, byteorder="big")
                    else:
                        print("c is not letter")
                        shift = int.from_bytes(key[index].encode())
                        byte = (int.from_bytes(c.encode()) + shift).to_bytes(4, byteorder="big")

                    index += 1
                    res.extend(byte.rjust(4, b'\x00'))

        self.encoded_message = res
        print(res)

        return res

    def decode_message(self) -> bytearray:
        res = bytearray()

        return res