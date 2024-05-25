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

def get_input():
    return int(input("Enter the input: "))

# Implement factorial with memoization
factorial_memo = {}

def factorial(n):
    if n == 0:
        return 1
    if n in factorial_memo:
        return factorial_memo[n]
    result = n
    for i in range(n - 1, 0, -1):
        result *= i
    factorial_memo[n] = result
    return result

# Implement nCr with memoization
nCr_memo = {}

def nCr(n, r):
    if (n, r) in nCr_memo:
        return nCr_memo[(n, r)]
    result = factorial(n) // (factorial(r) * factorial(n - r))
    nCr_memo[(n, r)] = result
    return result

def count_over_input(input_value):
    count = 0
    for n in range(1, 101):
        for r in range(1, n):
            if nCr(n, r) > input_value:
                count += 1
    return count

def main():
    input_value = get_input()
    result = count_over_input(input_value)
    print(result)

main()
