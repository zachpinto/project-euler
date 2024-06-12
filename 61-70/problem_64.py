"""
Problem 64

Odd period square roots

All square roots are periodic when written as continued fractions and can be written in the form:

√N = a0 + 1 / (a1 + 1 / (a2 + 1 / (a3 + ...)))

For example, let us consider √23:

√23 = 4 + √23 - 4 = 4 + 1 / (1 / (√23 - 4)) = 4 + 1 / (1 + (√23 - 3) / 7)

If we continue we would get the following expansion:

√23 = 4 + 1 / (1 + 1 / (3 + 1 / (1 + 1 / (8 + ...))))

The process can be summarised as follows:

a0 = 4, 1 / (√23 - 4) = (√23 + 4) / 7 = 1 + (√23 - 3) / 7
a1 = 1, 7 / (√23 - 3) = 7(√23 + 3) / 14 = 3 + (√23 - 3) / 2
a2 = 3, 2 / (√23 - 3) = 2(√23 + 3) / 14 = 1 + (√23 - 4) / 7
a3 = 1, 7 / (√23 - 4) = 7(√23 + 4) / 7 = 8 + √23 - 4
a4 = 8, 1 / (√23 - 4) = (√23 + 4) / 7 = 1 + (√23 - 3) / 7
a5 = 1, 7 / (√23 - 3) = 7(√23 + 3) / 14 = 3 + (√23 - 3) / 2
a6 = 3, 2 / (√23 - 3) = 2(√23 + 3) / 14 = 1 + (√23 - 4) / 7
a7 = 1, 7 / (√23 - 4) = 7(√23 + 4) / 7 = 8 + √23 - 4

It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate
that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?
"""

import math


def user_input():
    limit = int(input("Enter the limit N: "))
    return limit


def continued_fraction_sqrt(n):
    """Returns the continued fraction representation of the square root of n."""
    m = 0
    d = 1
    a0 = a = int(math.sqrt(n))
    period = []

    if a * a == n:
        return (a0, [])

    while True:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        period.append(a)

        if a == 2 * a0:
            break

    return (a0, period)


def odd_period_count(limit):
    """Returns the count of numbers <= limit whose continued fraction representation of their square root has an odd period."""
    count = 0

    for n in range(2, limit + 1):
        _, period = continued_fraction_sqrt(n)
        if len(period) % 2 == 1:
            count += 1

    return count


def main():
    limit = user_input()
    result = odd_period_count(limit)
    print(f"The number of continued fractions for N ≤ {limit} with an odd period is: {result}")


main()
