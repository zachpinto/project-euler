"""
Problem 73: Counting fractions in a range

Consider the fraction, n/d, where n and d are positive integers. If n < d and HCF(n, d) = 1, it is called a reduced

proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
"""

from fractions import Fraction
from math import gcd


def user_input():
    limit = int(input("Enter the limit: "))
    return limit


def count_fractions(limit):
    count = 0
    lower_bound = Fraction(1, 3)
    upper_bound = Fraction(1, 2)

    for d in range(2, limit + 1):
        start_n = d // 3 + 1
        end_n = (d - 1) // 2 + 1

        for n in range(start_n, end_n):
            if gcd(n, d) == 1:
                fraction = Fraction(n, d)
                if lower_bound < fraction < upper_bound:
                    count += 1
    return count


def main():
    limit = user_input()
    result = count_fractions(limit)
    print(f"The number of fractions between 1/3 and 1/2 for d ≤ {limit} is {result}")


main()
