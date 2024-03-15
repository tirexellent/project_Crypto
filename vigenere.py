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
            key_index = 0
            for i in range(1, len(m)+1):
                c = m[i].lower()

                if i % 4 == 0:
                    key_index += 1


                # TODO: This
                if c in alph:
                    # print(f"{c} is letter")
                    shift = alph.index(key[key_index].lower())
                else:
                    # print(f"{c} is not letter")
                    shift = int.from_bytes(key[key_index].encode())
                    
                print(f"{c} will be shifted by {shift}")
                byte = (int.from_bytes(c.encode()) + shift).to_bytes(4, byteorder="big")

                res.extend(byte.rjust(4, b'\x00'))

        self.encoded_message = res
        return res

    def decode_message(self) -> bytearray:
        res = bytearray()

        return res
    
    def run_state(self, state, s, msg_size) -> None:
        # read ISC + type
        if state == 1:
            rcv = s.recv(4)
            print(f"rcv {state} {rcv}")
        # read msg length
        if state == 2:
            rcv = s.recv(2)
            print(f"rcv {state} {rcv}")
            self.info_msg_size = int.from_bytes(rcv)
        # read info with key
        if state == 3:
            rcv = s.recv(self.info_msg_size*4)
            print(f"rcv {state} {rcv.decode()}")
            if self.key == "":
                self.key = str(rcv.decode().split()[-1])
        # read msg to encrypt
        if state == 4:
            rcv = s.recv(6 + msg_size*4)
            print(f"rcv {state} {rcv.decode()}")

            if self.message == "":  
                self.message = rcv.decode()[6:]

            self.encode_message()
            
