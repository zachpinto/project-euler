# Problem 47

# Distinct primes factors

# The first two consecutive numbers to have two distinct prime factors are:

# 14 = 2 × 7
# 15 = 3 × 5

# The first three consecutive numbers to have three distinct prime factors are:

# 644 = 2^2 × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.

# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

def prime_factors_sieve(limit):
    factors = [[] for _ in range(limit)]
    for i in range(2, limit):
        if not factors[i]:  # i is prime
            for j in range(i, limit, i):
                k = j
                while k % i == 0:
                    k //= i
                factors[j].append(i)
    return factors


def find_consecutive_numbers(num_factors, consecutive):
    limit = 10 ** 6  # You can adjust the limit based on the problem's requirements.
    factor_counts = prime_factors_sieve(limit)

    count = 0
    for i in range(2, limit):
        if len(factor_counts[i]) == num_factors:
            count += 1
        else:
            count = 0

        if count == consecutive:
            return i - consecutive + 1


def main():
    # We are looking for the first four consecutive integers with exactly four distinct prime factors.
    result = find_consecutive_numbers(4, 4)
    print(result)


main()
