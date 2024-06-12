"""
Problem 71: Ordered fractions

Consider the fraction, n/d, where n and d are positive integers. If n < d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 1/3, 2/5, 1/2, 3/5, 2/3, 3/4, 4/5, 5/6, 5/7, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
"""

# list set of redued proper fractions for d <= limit in ascending order of size
# find numerator of the fraction immediately to the left of 3/7

def user_input():
    limit = int(input("Enter the limit: "))
    return limit

def fraction_input():
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    return numerator, denominator

def gcd(a, b):
    """Returns the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def find_fraction_left_of_target(limit, target_numerator, target_denominator):
    target_fraction = target_numerator / target_denominator
    closest_numerator = 0
    closest_denominator = 1
    closest_value = 0

    for d in range(2, limit + 1):
        n = (d * target_numerator) // target_denominator
        if gcd(n, d) == 1:
            value = n / d
            if value < target_fraction and value > closest_value:
                closest_numerator = n
                closest_denominator = d
                closest_value = value

    return closest_numerator, closest_denominator

def main():
    limit = user_input()
    target_numerator, target_denominator = fraction_input()
    closest_numerator, closest_denominator = find_fraction_left_of_target(limit, target_numerator, target_denominator)
    if closest_numerator:
        print(f"The numerator of the fraction immediately to the left of {target_numerator}/{target_denominator} is {closest_numerator}")
    else:
        print("No fraction found immediately to the left.")

main()
