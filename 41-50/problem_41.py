from itertools import permutations

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def largest_pandigital_prime():
    """Find the largest pandigital prime."""
    # Check pandigital numbers from largest set to smallest
    for num_digits in range(9, 0, -1):
        pandigitals = permutations('123456789'[:num_digits])
        for pandigital in sorted(pandigitals, reverse=True):
            number = int(''.join(pandigital))
            if is_prime(number):
                return number


def main():
    result = largest_pandigital_prime()
    print(result)


main()
