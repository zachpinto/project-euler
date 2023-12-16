# Problem 14
# Longest Collatz sequence

# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been
# proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

def even(n):
  n = n/2
  return n

def odd(n):
  n = 3*n + 1
  return n

def collatz(n):
  count = 0

  while n!= 1:
    if n % 2 == 0:
      n = even(n)
    else:
      n = odd(n)
    count += 1

  return count

def main():
  best_i = 1
  max_count = 0

  for i in range(1, 1000001):
    count = collatz(i)
    if count > max_count:
      max_count = count
      best_i = i

  return best_i

main()
