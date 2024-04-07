# Problem 33

# Digit cancelling fractions

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from fractions import Fraction

def find_digit_cancelling_fractions():
    product = 1

    for numerator in range(10, 100):
        for denominator in range(numerator + 1, 100):
            if numerator % 10 == 0 and denominator % 10 == 0:
                continue

            common = set(str(numerator)) & set(str(denominator))
            if len(common) == 1:
                common_digit = common.pop()
                new_numerator = int(str(numerator).replace(common_digit, '', 1))
                new_denominator = int(str(denominator).replace(common_digit, '', 1))

                if new_denominator != 0 and Fraction(numerator, denominator) == Fraction(new_numerator, new_denominator):
                    product *= Fraction(numerator, denominator)

    return product.denominator


def main():
    print(find_digit_cancelling_fractions())


main()