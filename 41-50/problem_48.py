# Problem 48

# Title: Self powers

# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

def user_input():
  n = int(input("Please choose a number n such that for numbers 1-n, we find the sum of all numbers n^n: "))
  return n


def self_powers(n):
  self_powers_sum = 0

  for i in range(1, n + 1):
    self_powers_sum += i ** i

  self_powers_sum = str(self_powers_sum)

  return self_powers_sum[-10:]


def main():
  n = user_input()
  result = self_powers(n)

  return result


main()
