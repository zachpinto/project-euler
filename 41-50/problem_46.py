# Problem 46

# Goldbach's other conjecture

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

# 9 = 7 + 2×1^2

# 15 = 7 + 2×2^2

# 21 = 3 + 2×3^2

# 25 = 7 + 2×3^2

# 27 = 19 + 2×2^2

# 33 = 31 + 2×1^2

# It turns out that the conjecture was false.

# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_goldbach(n):
    for i in range(1, int(math.sqrt(n)) + 1):
        if is_prime(n - 2 * i **2):
            return True

    return False


def find_odd_composite():
    n = 3
    while True:
        if not is_prime(n):
            if not is_goldbach(n):
                return n
        n += 2


def main():
    print(find_odd_composite())


main()
