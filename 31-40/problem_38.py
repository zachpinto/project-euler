# Problem 38

# Pandigital multiples

# Take the number 192 and multiply it by each of 1, 2, and 3:

# 192 x 1 = 192

# 192 x 2 = 384

# 192 x 3 = 576

# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1, 2, 3).

# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1, 2, 3, 4, 5).

# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer and (1, 2, ..., n) where n > 1?

def pandigital_multiple(n, list1):
  string1 = ""

  for i in list1:
    x = i * n
    x = str(x)
    string1 += x

  if len(string1) != 9:
    return False

  for i in range(1, 10):
    if str(i) not in string1:
      return False

  return string1


def biggest_pandigital_multiple():
  biggest = 918273645

  # assuming max 999 int
  for i in range(9,10000000):
    x = pandigital_multiple(i, [1,2])
    biggest = max(biggest, int(x))
    x = pandigital_multiple(i, [1,2,3])
    biggest = max(biggest, int(x))
    x = pandigital_multiple(i, [1,2,3,4])
    biggest = max(biggest, int(x))
    x = pandigital_multiple(i, [1,2,3,4,5])
    biggest = max(biggest, int(x))

  return biggest


def main():
  result = biggest_pandigital_multiple()
  return result


main()
