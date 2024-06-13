"""
Problem 77: Prime summations

It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
"""

from math import isqrt

def user_input():
    limit = int(input("Enter the limit: "))
    return limit


def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, isqrt(limit) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False

    return [i for i, prime in enumerate(primes) if prime]


def count_prime_summations(limit):
    primes = sieve_of_eratosthenes(limit)
    ways = [0] * (limit + 1)
    ways[0] = 1

    for prime in primes:
        for i in range(prime, limit + 1):
            ways[i] += ways[i - prime]

    for i, ways_count in enumerate(ways):
        if ways_count > 5000:
            return i


def main():
    limit = user_input()
    result = count_prime_summations(limit)
    print(f"The first value which can be written as the sum of primes in over five thousand different ways is {result}")


main()
