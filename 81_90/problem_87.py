"""
Problem 87

Prime power triples

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

    28 = 2^2 + 2^3 + 2^4

    33 = 3^2 + 2^3 + 2^4

    49 = 5^2 + 2^3 + 2^4

    47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""

import sympy

def user_input():
    limit = int(input("Please choose a limit: "))
    return limit


def generate_prime_powers(limit):
    list_2p = []
    list_3p = []
    list_4p = []
    for prime in sympy.primerange(1, int(limit ** 0.5) + 1):
        list_2p.append(prime ** 2)
    for prime in sympy.primerange(1, int(limit ** (1/3)) + 1):
        list_3p.append(prime ** 3)
    for prime in sympy.primerange(1, int(limit ** 0.25) + 1):
        list_4p.append(prime ** 4)
    return list_2p, list_3p, list_4p


def prime_power_triples(limit, list_2p, list_3p, list_4p):
    prime_power_triples_set = set()
    for i in list_2p:
        for j in list_3p:
            for k in list_4p:
                sum_powers = i + j + k
                if sum_powers < limit:
                    prime_power_triples_set.add(sum_powers)
                else:
                    break
    return len(prime_power_triples_set)


def main():
    limit = user_input()
    list_2p, list_3p, list_4p = generate_prime_powers(limit)
    result = prime_power_triples(limit, list_2p, list_3p, list_4p)
    print(f"Result: {result}")


main()
