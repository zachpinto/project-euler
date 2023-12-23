# Problem 16
# Power digit sum

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

def get_user_input():
  try:
    n = int(input("Please choose a power for the number 2: "))
    return n
  except ValueError:
    print("Invalid input. Please enter a valid integer.")
    return None

def power(n):
  n = 2 ** n
  return n

def sum_digits_power(n):
  n_str = str(n)

  sum = 0

  for i in n_str:
    i = int(i)
    sum += i

  return sum


def main():
  n = get_user_input()
  n = power(n)
  result = sum_digits_power(n)
  return result


main()
