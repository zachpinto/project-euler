"""
Problem 66

Diophantine equation

Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
"""

import math


def user_input():
    limit = int(input("Please enter the limit (D): "))
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


def minimal_solution_x(d):
    """Find the minimal solution x for x^2 - d*y^2 = 1."""
    a0, period = continued_fraction_sqrt(d)
    period_length = len(period)

    if period_length == 0:
        return None  # No solution if d is a perfect square

    # Build the continued fraction sequence
    cf_sequence = [a0] + period * (2 * period_length)

    h0, h1 = cf_sequence[0], cf_sequence[0] * cf_sequence[1] + 1
    k0, k1 = 1, cf_sequence[1]

    for i in range(2, len(cf_sequence)):
        h2 = cf_sequence[i] * h1 + h0
        k2 = cf_sequence[i] * k1 + k0

        h0, h1 = h1, h2
        k0, k1 = k1, k2

        if h1 * h1 - d * k1 * k1 == 1:
            return h1

    return None


def find_largest_x(limit):
    max_x = 0
    result_d = 0

    for d in range(2, limit + 1):
        if int(math.sqrt(d)) ** 2 == d:
            continue  # Skip perfect squares

        x = minimal_solution_x(d)
        if x is not None and x > max_x:
            max_x = x
            result_d = d

    return result_d


def main():
    limit = user_input()
    result = find_largest_x(limit)
    print(f"The value of D ≤ {limit} in minimal solutions of x for which the largest value of x is obtained is: {result}")


main()
