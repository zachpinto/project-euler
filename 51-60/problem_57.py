"""
Problem 57

Square root convergents

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""

from fractions import Fraction

def user_input():
    limit = int(input("Please choose a limit: "))
    return limit

def square_root_convergents(limit):
    count = 0
    fraction = Fraction(1, 2)
    for i in range(1, limit + 1):
        fraction = 1 / (2 + fraction)
        expansion = 1 + fraction
        if len(str(expansion.numerator)) > len(str(expansion.denominator)):
            count += 1
    return count

def main():
    limit = user_input()
    result = square_root_convergents(limit)
    print(f"Result: {result}")

main()


