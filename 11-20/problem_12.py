# Problem 12
# Highly divisible triangular number

# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
# The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

# Let us list the factors of the first seven triangle numbers:
# 1: 1
# 3: 1, 3
# 6: 1, 2, 3, 6
# 10: 1, 2, 5, 10
# 15: 1, 3, 5, 15
# 21: 1, 3, 7, 21
# 28: 1, 2, 4, 7, 14, 28

# We can see that 28 is the first triangle number to have over five divisors

# What is the value of the first triangle number to have over n divisors?


def get_user_input():
    try:
        user_input = int(input("Enter a number: "))
        return user_input
    except ValueError:
        print("Please enter a valid number")
        return get_user_input()


def triangle_number(n):
    return n * (n + 1) // 2


def number_of_divisors(triangle_number):
    divisors = 0

    for i in range(1, int(triangle_number ** 0.5) + 1):
        if triangle_number % i == 0:
            divisors += 2

    return divisors


def highly_divisible_triangular_number(user_input):
    i = 1

    divisors = 0

    while divisors < user_input:
        triangle_num = triangle_number(i)
        divisors = number_of_divisors(triangle_num)
        i += 1

    return triangle_num


def main():
    user_input = get_user_input()
    print(
        f"You chose {user_input}. This means will we find the first triangle number to have over {user_input} divisors.")
    result = highly_divisible_triangular_number(user_input)
    print(f"The first triangle number is {result}.")


main()