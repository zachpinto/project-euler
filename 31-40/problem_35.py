# Problem 35

# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are

# themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?


def user_input():
    n = int(input("Choose a number n such that we will find the # of circular primes below n: "))
    return n


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False

    return True


def rotate(n):
    n = str(n)

    all_n_rotations = []

    for i in range(len(n)):
        all_n_rotations.append(int(n[i:] + n[:i]))

    return all_n_rotations


def is_circular_prime(n):
    if not is_prime(n):
        return False

    for rotation in rotate(n):
        if not is_prime(rotation):
            return False

    return True


def main():
    n = user_input()
    count = 0

    for i in range(2, n + 1):
        if is_circular_prime(i):
            count += 1

    print(count)


main()
