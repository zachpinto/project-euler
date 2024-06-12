"""
Problem 72: Counting fractions

Consider the fraction, n/d, where n and d are positive integers. If n < d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 1/3, 2/5, 1/2, 3/5, 2/3, 3/4, 4/5, 5/6, 5/7, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
"""

# list set of redued proper fractions for d <= limit in ascending order of size
# find the number of elements in the set

def user_input():
    limit = int(input("Enter the limit: "))
    return limit

def count_fractions(limit):
    phi = list(range(limit + 1))

    for i in range(2, limit + 1):
        if phi[i] == i:  # i is a prime number
            for j in range(i, limit + 1, i):
                phi[j] = phi[j] * (i - 1) // i

    return sum(phi) - 1  # Subtract 1 to exclude the fraction 1/1

def main():
    limit = user_input()
    count = count_fractions(limit)
    print(f"The number of elements in the set of reduced proper fractions for d <= {limit} is {count}")

main()
