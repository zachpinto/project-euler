"""
Problem 80

Square root digital expansion

It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""

from decimal import Decimal, getcontext

def user_input():
    limit = int(input("Enter the limit: "))
    return limit


def square_root_digit_sum(limit):
    getcontext().prec = 102
    total_sum = 0

    for n in range(1, limit + 1):
        root = Decimal(n).sqrt()
        if int(root) ** 2 != n:
            total_sum += sum(int(digit) for digit in str(root)[:101].replace(".", ""))

    return total_sum


def main():
    limit = user_input()
    result = square_root_digit_sum(limit)
    print(f"The total of the digital sums of the first one hundred decimal digits for all the irrational square roots of the first one hundred natural numbers is {result}")


main()
