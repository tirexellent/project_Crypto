def modpow(a: int, e: int, n: int):
    result: int = 1

    while e > 0:
        if (e & 1) > 0:
            result = (result * a) % n

        e >>= 1
        a = (a * a) % n

    return result