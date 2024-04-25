from server_socket import Socket
from message import Message
from rsa import RSA
import conversion

TYPE = "t"

def chat(s: Socket):
    print("Listen/send ? [l/s]"),
    task = input()
    
    try: 
        match alg:
            case "RSA":
                rsa = RSA()
                if task == "encode":
                    rsa.start_encoding(s, TYPE)

                elif task == "decode":
                    s.receive_str(TYPE)
                    keys = f"{rsa.publicKey[0]},{rsa.publicKey[1]}"
                    s.send_str(TYPE, keys)
                    msg_to_decode = s.receive_bytes(TYPE)
                    decoded_msg = rsa.decode_message(msg_to_decode)
                    s.send_bytes(TYPE, decoded_msg)

                    res = s.receive_str(TYPE)
                    print(res)

            case "DiffHell":
                if task == "encode":
                    dh_encode()

        s.reconnect()
    except Exception as err:
        raise err
    else:
        pass
def rsa_encode():
    pass

def dh_encode():
    pass