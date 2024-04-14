# Problem 37

# Truncatable primes

# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly, we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def is_truncatable_prime(n):
    n_str = str(n)

    for i in range(1, len(n_str)):
        if not is_prime(int(n_str[i:])):
            return False
        if not is_prime(int(n_str[:i])):
            return False

    return True


def find_truncatable_primes():
    truncatable_primes = []
    n = 11

    while len(truncatable_primes) < 11:
        if is_prime(n) and is_truncatable_prime(n):
            truncatable_primes.append(n)
        n += 2

    return sum(truncatable_primes)


def main():
    print(find_truncatable_primes())


main()
