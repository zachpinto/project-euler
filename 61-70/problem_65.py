"""
Problem 65: Convergents of e

The square root of 2 can be written as an infinite continued fraction.

√2 = 1 + 1/(2 + 1/(2 + 1/(2 + ...)))

The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates that 2 repeats ad infinitum. In a similar way,

√23 = [4;(1,3,1,8)].

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations.

Let us consider the convergents for √2.

1 + 1/2 = 3/2
1 + 1/(2 + 1/2) = 7/5
1 + 1/(2 + 1/(2 + 1/2)) = 17/12
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29

Hence the sequence of the first ten convergents for √2 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the important mathematical constant,

e = [2; 1,2,1, 1,4,1, 1,6,1, ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1 + 4 + 5 + 7 = 17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
"""


from fractions import Fraction


def user_input():
    convergent = int(input("Please enter convergent: "))
    return convergent


def generate_e_sequence(n):
    """Generate the first n terms of the continued fraction sequence for e."""
    sequence = [2]
    k = 1
    while len(sequence) < n:
        sequence.extend([1, 2 * k, 1])
        k += 1
    return sequence[:n]


def compute_convergent(sequence):
    """Compute the convergent from the continued fraction sequence."""
    convergent = Fraction(sequence[-1])
    for term in reversed(sequence[:-1]):
        convergent = term + 1 / convergent
    return convergent


def sum_of_digits(number):
    """Calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(number))


def main():
    convergent_index = user_input()
    sequence = generate_e_sequence(convergent_index)
    convergent = compute_convergent(sequence)
    numerator = convergent.numerator
    result = sum_of_digits(numerator)
    print(f"The sum of digits in the numerator of the {convergent_index}th convergent of e is: {result}")


main()
