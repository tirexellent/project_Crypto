from server_socket import Socket
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

    correct = False
    res = ""
    while(not correct):
        s.send_str(TYPE, m)

        try: 
            match alg:
                case "shift":
                    shift = Shift()
                    if task == "encode":
                        res = shift.start_encoding(s, TYPE)
                    elif task == "decode":
                        res = shift.start_decoding(s, TYPE)
                        
                case "vigenere":
                    vigenere = Vigenere()
                    if task == "encode":
                        res = vigenere.start_encoding(s, TYPE)
                    elif task == "decode":
                        res = vigenere.start_decoding(s, TYPE)

                case "RSA":
                    rsa = RSA()
                    if task == "encode":
                        res = rsa.start_encoding(s, TYPE)
                    elif task == "decode":
                        res = rsa.start_decoding(s, TYPE)

                case "DifHel":
                    dh = DiffieHellman()
                    res = dh.start(s, TYPE)
        
            correct = " correct" in res or " valid" in res
            s.reconnect()
        except Exception as err:
            raise err
        else:
            pass
        
def rsa_encode():
    pass

def dh_encode():
    pass