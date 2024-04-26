from RSAKeyGenerator import RSAKeyGenerator
from message import Message
import random
import utils

class RSA():
    def __init__(self):
        self.keygen = RSAKeyGenerator()

        self.keygen.p = self.keygen.getRandomPrime() # random.choice(self.keygen.primes)
        self.keygen.q = self.keygen.getRandomPrime() # random.choice(self.keygen.primes)
        self.keygen.n = self.keygen.p * self.keygen.q
        self.keygen.k = (self.keygen.p - 1) * (self.keygen.q - 1)
        self.keygen.e = random.randint(2, self.keygen.k - 1)
        self.keygen.b = 0

        self.setKeys()

    def start_encoding(self, s, t):
        keys = s.receive_str(t)
        self.getKey(keys)
        msg_to_encode = s.receive_bytes(t)
        print("Message: ", msg_to_encode.decode())
        encoded_msg = self.encode_message(msg_to_encode)
        s.send_bytes(t,  encoded_msg)

        return s.receive_str(t)

    def start_decoding(self, s, t):        
        s.receive_str(t)
        keys = f"{self.publicKey[0]},{self.publicKey[1]}"
        s.send_str(t, keys)
        msg_to_decode = s.receive_bytes(t)
        print("Message, ", msg_to_decode)
        decoded_msg = self.decode_message(msg_to_decode)
        s.send_bytes(t, decoded_msg)

        return s.receive_str(t)

    def encode_message(self, msg):
        encoded_message = bytes()
        for four_bytes in Message.message_to_4_bytes_array(msg):
            z = utils.modpow(int.from_bytes(four_bytes), self.keygen.e, self.keygen.n)
            encoded_message += z.to_bytes(4)


        print("Encoded", encoded_message)
        return encoded_message

    def decode_message(self, msg):
        decoded_message = bytes()
        for four_bytes in Message.message_to_4_bytes_array(msg):
            z = utils.modpow(int.from_bytes(four_bytes), self.keygen.d, self.keygen.n)
            decoded_message += z.to_bytes(4,"big")

        print("Decoded", decoded_message)
        return decoded_message

    # Only for server
    def getKey(self, rcv: str) -> None:
        s = rcv.split("=")

        self.keygen.n = int(s[1].split(",")[0])
        self.keygen.e = int(s[-1])
        
        self.setKeys()

    def setKeys(self):
        self.keygen.d = self.keygen.find_d(self.keygen.k, self.keygen.e)
        self.publicKey = (self.keygen.n, self.keygen.e)
        self.privateKey = (self.keygen.n, self.keygen.d)
