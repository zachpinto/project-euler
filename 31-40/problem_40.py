# Problem 40

# Title: Champernowne's constant

# An irrational decimal fraction is created by concatenating the positive integers:

# 0.123456789101112131415161718192021...

# It can be seen that the 12th digit of the fractional part is 1.

# If dn represents the nth digit of the fractional part, find the value of the following expression.

# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

def concat_pos_int_decimal():
  decimal = '0.'
  for i in range(1,1000000):
    i = str(i)
    decimal += i

  return decimal[2:]


def main():
  decimal = concat_pos_int_decimal()

  result = int(decimal[0]) * int(decimal[9]) * int(decimal[99]) * int(decimal[999]) * int(decimal[9999]) * int(decimal[99999]) * int(decimal[999999])

  return result


main()
