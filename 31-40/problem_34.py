# Problem 34

# Title: Digit factorials

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

def user_input():
  n = int(input("Please choose a number n such that 1-n: "))
  return n


def factorial(n):
  factorial = 1

  for i in range(n, 0, -1):
    factorial *= i

  return factorial


def factorial_sum(n):
  num = str(n)

  factorial_sum = 0

  for digit in num:
    digit = int(digit)
    factorial_result = factorial(digit)
    factorial_sum += factorial_result

  return factorial_sum


def main():
  n = user_input()

  curious_nums = []

  for i in range(3, n):
    if i == factorial_sum(i):
      curious_nums.append(i)

  result = len(curious_nums)

  sum = 0

  for i in curious_nums:
    sum += i

  print(f"There are {result} numbers between 1-{n} that are curious numbers.")
  print(f"The numbers are: {curious_nums}.")
  print(f"The sum of these numbers is: {sum}.")


main()
