# Problem 43

# Sub-string divisibility

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7

# Find the sum of all 0 to 9 pandigital numbers with this property.

import itertools

def is_sub_string_divisible(n):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        if int(n[i:i+3]) % primes[i - 1] != 0:
            return False
    return True


def sum_pandigital_ssd_property():
    pandigital_numbers = itertools.permutations('0123456789')
    total = 0
    for number in pandigital_numbers:
        number = ''.join(number)
        if is_sub_string_divisible(number):
            total += int(number)
    return total


def main():
    print(sum_pandigital_ssd_property())


main()
