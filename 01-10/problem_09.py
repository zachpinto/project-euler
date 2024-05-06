# Problem 9
# Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which a^2 + b^2 = c^2

# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc

def special_pythagorean_triplet():
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c


def main():
    result = special_pythagorean_triplet()
    print(f"The product of the Pythagorean triplet is {result}.")


main()
