# Problem 63

# Powerful digit counts

# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

# How many n-digit positive integers exist which are also an nth power?

def powerful_digit_counts():
  powerful_digit_count = 0
  # base
  for i in range(1, 50):
    # power
    for j in range(1, 50):
      result = i ** j
      if len(str(result)) == j:
        powerful_digit_count += 1

  return powerful_digit_count


powerful_digit_counts()
