import random

primes = []

def generate_primes(n):
    for possiblePrime in range(2, n + 1):
        is_prime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(possiblePrime)
    return primes


# Example usage:
maxNum = 10000000
generate_primes(maxNum)

def gcd(x, y):
    # Use Euclid's algorithm to find the GCD.
    while y != 0:
        x, y = y, x % y
    return x


# Define a function 'is_coprime' to check if two numbers are coprime (GCD is 1).
def is_coprime(e, k):
    # Check if the GCD of 'x' and 'y' is equal to 1.
    return gcd(e, k) == 1





def find_d(k, e):
    L1 = [e, 1, 0]
    L2 = [k, 0, 1]
    while L2[0] != 0:
        q = L1[0] // L2[0]
        L = L2[:]
        for i in range(0, 3):
            L2[i] = L1[i] - q * L2[i]
        L1 = L
    if L1[1] >= 0:
        return L1[1]
    else:
        return L1[1]+k





def modpow(a, e, n):
    result = 1

    while e > 0:
        if (e & 1) > 0:
            result = (result * a) % n

        e >>= 1
        a = (a * a) % n

    return result




while True:
    start = input("type 's' to generate key set: ")
    if start == 's':
        p = random.choice(primes)
        q = random.choice(primes)
        n = p * q
        k = (p - 1) * (q - 1)
        e = random.randint(2, k - 1)
        b = 0

        while not is_coprime(e, k):
            e = random.randint(2, k - 1)

        d = find_d(k, e)
        publicKey = (n, e)
        privateKey = (n, d)

        print(publicKey)
        print(privateKey)

        a = 18
        z = modpow(a, e, n)
        print(a)
        print(z)
        solved = modpow(z, d, n)
        print(solved)
