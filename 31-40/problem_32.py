# Problem 32
# Pandigital products

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

def is_pandigital(num):
    return len(num) == 9 and not '123456789'.strip(num)


def pandigital_products():
    products = set()

    for i in range(1, 100):
        for j in range(i, 10000):
            product = i * j
            num = str(i) + str(j) + str(product)
            if len(num) > 9:
                break
            if is_pandigital(num):
                products.add(product)

    return sum(products)


def main():
    result = pandigital_products()
    print(
        f"The sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital is {result}.")


main()
