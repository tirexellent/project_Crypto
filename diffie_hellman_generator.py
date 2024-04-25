import utils
import random
import math

def generate_common_prime():
    return getRandomPrime()

def getRandomPrime():
    f = open("primes.0001", "r") # 0 to 5000
    return int(random.choice(f.readlines()))

def generate_generator(p, primes): # p == n
    for g in range(2, p-1):
        is_generator = True
        if g not in primes:
            for a in range(2, p-1):
                res = utils.modpow(g,a,p)
                # print(f"{g}**{j} % {p} = {res}")

                if res == 1:
                    is_generator = False
                    break
        else:
            for a in primes:
                a = (p-1)//a
                res = utils.modpow(g,a,p)
                # print(f"{g}**{a} % {p} = {res}")

                if res == 1:
                    is_generator = False
                    break

        if is_generator:
            return g
        g += 1

    return 0

def get_primes_below(p):
    lst = []
    f = open("primes.0001", "r")
    for n in f.readlines(p):
        lst.append(int(n))

    return lst

def get_half_key(g, p):
    b = math.ceil(random.random() * 100)
    return utils.modpow(g, b, p)