class Algorithm:
    def __init__(self, m: str = "", k: int | str = ""):
        self.message = m
        self.key = k

    def encode_message(self) -> bytearray:
        """Encode message"""
        pass

    def decode_message(self) -> bytearray:
        """Decode message"""
        pass

    def run_state(self, state, s, msg_size) -> None:
        """test with server"""
        pass