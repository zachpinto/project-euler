# Problem 51

# Prime digit replacements

# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

from itertools import combinations, product

def sieve_of_eratosthenes(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for i in range(start*start, limit, start):
                sieve[i] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]

def prime_digit_replacements(primes, family_size):
    prime_set = set(primes)
    for prime in primes:
        s = str(prime)
        length = len(s)
        # Try replacing every possible non-empty subset of indices with each digit from 0 to 9
        for r in range(1, length):  # r is the number of digits replaced
            for indices in combinations(range(length), r):
                prime_family = set()
                # Replace selected digits with each digit from 0 to 9
                for replacement_digit in map(str, range(10)):
                    if indices[0] == 0 and replacement_digit == '0':
                        continue  # Skip leading zero cases
                    new_number = list(s)
                    for index in indices:
                        new_number[index] = replacement_digit
                    new_prime = int(''.join(new_number))
                    if new_prime in prime_set:
                        prime_family.add(new_prime)
                if len(prime_family) == family_size:
                    return prime
    return None

def main():
    primes = sieve_of_eratosthenes(100000)
    result = prime_digit_replacements(primes, 8)
    print("The smallest prime in the family is:", result)

main()


