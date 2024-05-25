# Problem 53

# Combinatoric selections

# There are exactly ten ways of selecting three from five, 12345:

# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

# In combinatorics, we use the notation, 5C3 = 10.

# In general,

# nCr = n! / r!(n−r)!

# where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

# How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

# user input
def get_input():
    return int(input("Enter the input: "))

# implement factorial without using math.factorial
def factorial(n):
    if n == 0:
        return 1
    for i in range(n - 1, 0, -1):
        n *= i
    return n


# implement nCr
def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


def count_over_input(input):
    count = 0
    for n in range(1, 101):
        for r in range(1, n):
            if nCr(n, r) > input:
                count += 1
    return count


def main():
    input = get_input()
    result = count_over_input(input)
    print(result)


main()
