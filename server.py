from server_socket import Socket
from message import Message
from shift import Shift
from vigenere import Vigenere
from rsa import RSA
from diffie_hellman import DiffieHellman

TYPE = "s"

def chat(s: Socket):
    
    print("Which algorithm ?")
    alg = input()
    size = 8
    m = "task "
    if alg == "DifHel":
        m += alg
    else:
        print("Which task ?")
        task = input()
        m += f"{alg} {task} {size}"

    s.send_str(TYPE, m)
    
    try: 
        match alg:
            case "shift":
                shift = Shift()
                if task == "encode":
                    shift.start_encoding(s, TYPE)
                elif task == "decode":
                    shift.start_decoding(s, TYPE)
                    
            case "vigenere":
                vigenere = Vigenere()
                if task == "encode":
                    vigenere.start_encoding(s, TYPE)
                elif task == "decode":
                    vigenere.start_decoding(s, TYPE)

            case "RSA":
                rsa = RSA()
                if task == "encode":
                    rsa.start_encoding(s, TYPE)
                elif task == "decode":
                    rsa.start_decoding(s, TYPE)

            case "DifHel":
                dh = DiffieHellman()
                dh.start(s, TYPE)

        s.reconnect()
    except Exception as err:
        raise err
    else:
        pass
def rsa_encode():
    pass

def dh_encode():
    pass