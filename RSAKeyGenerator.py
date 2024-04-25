import random


class RSAKeyGenerator():
    def __init__(self) -> None:
        self.primes = []

    def generate_primes(self, n):
        for possiblePrime in range(2, n + 1):
            is_prime = True
            for num in range(2, int(possiblePrime ** 0.5) + 1):
                if possiblePrime % num == 0:
                    is_prime = False
                    break
            if is_prime:
                self.primes.append(possiblePrime)
        return self.primes
    

    # get random prime numbers in file
    def getRandomPrime(self):
        f = open("primes.0001", "r")
        return int(random.choice(f.readlines()))

    def gcd(self, x, y):
        # Use Euclid's algorithm to find the GCD.
        while y != 0:
            x, y = y, x % y
        return x


    # Define a function 'is_coprime' to check if two numbers are coprime (GCD is 1).
    def is_coprime(self, e, k):
        # Check if the GCD of 'x' and 'y' is equal to 1.
        return self.gcd(e, k) == 1

    def find_d(self, k, e):
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