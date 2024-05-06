# Problem 4
# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two n-digit numbers.

def get_user_input():
    try:
        user_input = int(input(
            "Enter a number: (Keep this a single digit number as the computation time increases exponentially with the number of digits.)"))
        return user_input
    except ValueError:
        print("Please enter a valid number")
        return get_user_input()


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def largest_palindrome_product(user_input):
    largest_palindrome = 0

    start = 10 ** (user_input - 1)
    end = 10 ** user_input

    for i in range(start, end):
        for j in range(start, end):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome


def main():
    user_input = get_user_input()
    print(
        f"You chose {user_input}. This means will we find the largest palindrome made from the product of two {user_input}-digit numbers.")
    result = largest_palindrome_product(user_input)
    print(f"The largest palindrome is {result}.")


main()
