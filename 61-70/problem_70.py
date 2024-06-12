"""
Problem 70

Totient permutation

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""

from math import isqrt

def user_input():
    limit = int(input("Enter the limit N: "))
    return limit


def sieve(limit):
    """Returns a list of prime numbers up to the limit."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for n in range(2, isqrt(limit) + 1):
        if sieve[n]:
            for i in range(n * n, limit + 1, n):
                sieve[i] = False

    return [n for n in range(2, limit + 1) if sieve[n]]


def prime_factors(n, primes):
    factors = []
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
    if n > 1:
        factors.append(n)
    return factors


def totient(n, primes):
    """Returns the value of Euler's Totient function φ(n)."""
    if n == 1:
        return 1

    factors = prime_factors(n, primes)
    result = n
    for p in factors:
        result *= (1 - 1 / p)
    return int(result)


def is_permutation(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))


def find_min_ratio(limit):
    primes = sieve(limit)
    min_ratio = float("inf")
    result = 0

    for n in range(2, limit):
        phi_n = totient(n, primes)
        if is_permutation(n, phi_n):
            ratio = n / phi_n
            if ratio < min_ratio:
                min_ratio = ratio
                result = n

    return result


def main():
    limit = user_input()
    result = find_min_ratio(limit)
    print(result)


main()
