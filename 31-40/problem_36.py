# Problem 36

# Title: Double-base palindromes

# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def user_input():
    n = int(input("Please choose a number n such that we find the sum of all numbers less than n that are palindromic in base 10 and base 2: "))
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def double_base_palindromes(n):
    sum = 0

    for i in range(1, n + 1):
        # check if i is a palindrome in base 10 and base 2
        # we slice the first two characters off to remove the '0b' from the binary representation
        if is_palindrome(i) and is_palindrome(bin(i)[2:]):
            sum += i

    return sum


def main():
    n = user_input()
    result = double_base_palindromes(n)
    print(result)


main()
