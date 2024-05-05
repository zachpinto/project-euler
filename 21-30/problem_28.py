# Problem 28

# Number spiral diagonals

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

# Solution:

def user_input():
    n = int(input("Choose a number n such that we will find the sum of the numbers on the diagonals in a n by n spiral: "))
    return n


def number_spiral_diagonals(n):
    if n == 1:
        return 1

    diagonal_sum = 1
    current_number = 1
    step = 2

    for i in range(1, n // 2 + 1):
        for j in range(4):
            current_number += step
            diagonal_sum += current_number

        step += 2

    return diagonal_sum


def main():
    n = user_input()
    print(number_spiral_diagonals(n))


main()