"""Problem 60

Prime pair sets

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order
the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime.

The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""



import sympy
from functools import lru_cache


def user_input():
    target_set_size = int(input("Enter the size of the set of primes: "))
    return target_set_size


@lru_cache(None)
def is_concat_prime(p1, p2):
    """Check if concatenating two numbers in any order results in primes."""
    return sympy.isprime(int(f"{p1}{p2}")) and sympy.isprime(int(f"{p2}{p1}"))


def find_prime_set(target_set_size=5, limit=10000):
    """Find the set of primes with the lowest sum where any two primes concatenate to a prime."""
    primes = list(sympy.primerange(1, limit))

    def search(current_set):
        if len(current_set) == target_set_size:
            return current_set

        for prime in primes:
            if prime > current_set[-1] and all(is_concat_prime(p, prime) for p in current_set):
                result = search(current_set + [prime])
                if result:
                    return result
        return None

    for prime in primes:
        result = search([prime])
        if result:
            return result, sum(result)

    return None, 0


def main():
    target_set_size = user_input()
    limit = 10000
    result, result_sum = find_prime_set(target_set_size, limit)
    print(f"Set of {target_set_size} primes: {result}")
    print(f"Sum of the set: {result_sum}")


main()
