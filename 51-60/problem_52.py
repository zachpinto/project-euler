# Problem 52
# Permuted multiples

# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.


from collections import Counter

def has_same_digits(n1, n2):
    return Counter(str(n1)) == Counter(str(n2))

def find_permuted_multiples():
    x = 1
    while True:
        if all(has_same_digits(x, x * i) for i in range(2, 7)):
            return x
        x += 1

def main():
    result = find_permuted_multiples()
    print("The smallest positive integer is:", result)

main()
