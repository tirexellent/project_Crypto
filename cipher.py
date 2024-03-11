class Cipher:
    def __init__(self, m: str, k: str | int):
        self.message = m
        self.key = k

    def encode_message(self) -> bytearray:
        """Encode message"""
        pass

    def decode_message(self) -> bytearray:
        """Decode message"""
        pass