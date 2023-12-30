# Problem 20
# Factorial Digit Sum

# n! means n * (n-1) * ... * 1
# 10! = 3628800
# sum of digits is 3+6+2+8+8+0+0 = 27

# Find the sum of digits of 100!


def get_user_input():
  try:
    n = int(input("Please choose a number: "))
    return n
  except ValueError:
    print("Invalid input. Please enter a valid integer.")
    return None


def factorial(n):
  total = n

  for i in range(n-1, 0, -1):
    total *= i

  return total


def num_to_digits(total):
  digits = str(total)

  list1 = []

  for i in digits:
    j = int(i)
    list1.append(j)

  return list1


def sum_of_digits(list1):
  sum = 0

  for i in list1:
    sum += i

  return sum


def main():
  n = get_user_input()
  total = factorial(n)
  list1 = num_to_digits(total)
  result = sum_of_digits(list1)
  return result


main()
