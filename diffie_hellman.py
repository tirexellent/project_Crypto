import utils
from message import Message
import random
import diffie_hellman_generator

class DiffieHellman():
    def __init__(self):
        pass
    
    def start(self, s, t):
        s.receive_str(t)
        p = diffie_hellman_generator.generate_common_prime()
        g = diffie_hellman_generator.generate_generator(
            p, diffie_hellman_generator.get_primes_below(p-1)
        )

        s.send_str(t, f"{p},{g}")
        s.receive_str(t)

        server_half_key = int(s.receive_str(t)) # g^b % p

        a = 7
        half_key_a = utils.modpow(g, a, p)

        secret = utils.modpow(server_half_key, a, p)

        print(half_key_a, secret)
        s.send_str(t, f"{half_key_a}")
        s.receive_str(t)
        s.send_str(t, f"{secret}")
        return s.receive_str(t)

    def encode_message(self, msg):
        pass

    def decode_message(self, msg):
        pass