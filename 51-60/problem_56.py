# Problem 56

# Powerful digit sum

# A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

def user_input():
  a = int(input("Please choose a number for a such that a ^ b: "))
  b = int(input("Please choose a number for b such that a ^ b: "))
  return a, b


def max_digital_sum(a, b):
  max_digital_sum = 0
  for i in range(1, a):
    for j in range(1, b):
      result = i ** j
      result = str(result)
      digital_sum = 0
      for char in result:
        digital_sum += int(char)
      max_digital_sum = max(max_digital_sum, digital_sum)

  return max_digital_sum


def main():
  a, b = user_input()
  result = max_digital_sum(a, b)
  return result


main()
