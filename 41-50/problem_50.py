# Problem 50

# Title: Consecutive prime sum

# The prime 41, can be written as the sum of six consecutive primes:

# 41 = 2 + 3 + 5 + 7 + 11 + 13

# This is the longest sum of consecutive primes that adds to a prime below one-hundred.

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

# Which prime, below one-million, can be written as the sum of the most consecutive primes?


def user_input():
    n = int(input("Please choose a number n such that we find the longest sum of consecutive primes below n: "))
    return n


def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for start in range(2, int(limit ** 0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, limit + 1, start):
                is_prime[multiple] = False
    return [num for num, prime in enumerate(is_prime) if prime]


def longest_sum_consec_primes_below_n(primes, n):
    prime_set = set(primes)
    max_sum = 0
    max_length = 0
    cumulative_sum = [0] * (len(primes) + 1)

    for i in range(len(primes)):
        cumulative_sum[i + 1] = cumulative_sum[i] + primes[i]

    for i in range(len(primes)):
        for j in range(i + max_length, len(primes)):
            current_sum = cumulative_sum[j + 1] - cumulative_sum[i]
            if current_sum >= n:
                break
            if current_sum in prime_set:
                max_length = j - i + 1
                max_sum = current_sum

    return max_sum, max_length


def main():
    n = user_input()
    primes = sieve_of_eratosthenes(n)
    max_sum, max_length = longest_sum_consec_primes_below_n(primes, n)
    print(
        f"The prime number below {n} that is the sum of the most consecutive primes is {max_sum} with {max_length} consecutive primes.")
    return max_sum, max_length


main()
