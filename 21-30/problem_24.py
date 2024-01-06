# Problem 24
# Title: Lexicographic permutations

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
# 012 021 102 120 201 210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


# for finding factorials
import math


def get_user_digit():
  digits = int(input("Choose a number of digits: "))
  return digits


def get_user_perm(digits):
  n = int(input(f"Choose n for the n-th permutaiton of the digits 0-{digits} to find: "))
  return n


def find_nth_permutation(digits, n):
  '''
  Finds the nth permutation of list of digits 0-n
  For example, will find the 1,000,000th permutation of digits 0-9
  Returns it as a string
  '''

  digit_list = []

  for i in range(0, digits+1):
    digit_list.append(i)

  permutation = []

  available_digits = digit_list[:]

  n -= 1

  while available_digits:
    factorial = math.factorial(len(available_digits) - 1)

    index = n // factorial

    permutation.append(available_digits.pop(index))

    n %= factorial

  return "".join(map(str, permutation))


def main():
  digits = get_user_digit()
  n = get_user_perm(digits)
  result = find_nth_permutation(digits, n)
  return result


main()
