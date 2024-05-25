# Problem 49

# Prime permutations

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

# What 12-digit number do you form by concatenating the three terms in this sequence?

from itertools import permutations

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_primes(start, end):
    primes = []
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
    return primes

def find_permutations(n):
    str_n = str(n)
    permutations_of_n = set(int(''.join(p)) for p in permutations(str_n) if p[0] != '0')
    return sorted(permutations_of_n)

def prime_permutations(primes):
    sequences = []
    primes_set = set(primes)
    for prime in primes:
        permutations_of_prime = find_permutations(prime)
        prime_permutations_of_prime = [p for p in permutations_of_prime if p in primes_set]
        prime_permutations_of_prime.sort()
        n = len(prime_permutations_of_prime)
        if n >= 3:
            for j in range(n):
                for k in range(j + 1, n):
                    diff = prime_permutations_of_prime[k] - prime_permutations_of_prime[j]
                    third_num = prime_permutations_of_prime[k] + diff
                    if third_num in prime_permutations_of_prime:
                        sequence = (prime_permutations_of_prime[j], prime_permutations_of_prime[k], third_num)
                        if sequence not in sequences:
                            sequences.append(sequence)
    return sequences

def main():
    primes = generate_primes(1000, 10000)
    sequences = prime_permutations(primes)
    for sequence in sequences:
        print(''.join(str(i) for i in sequence))

main()
