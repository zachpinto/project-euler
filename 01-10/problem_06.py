# Problem 6
# Sum square difference

# The sum of the squares of the first ten natural numbers is 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is (1 + 2 + ... + 10)^2 = 55^2 = 3025
# The difference between the sum of the squares and the square of the sum is 30215 - 385 = 2640

# The above problem uses 10 as input. Find the result for n

def get_user_input():
    try:
        user_input = int(input("Enter a number: "))
        return user_input
    except ValueError:
        print("Please enter a valid number")
        return get_user_input()


def sum_of_squares(user_input):
    sum = 0

    for i in range(1, user_input + 1):
        sum += i ** 2

    return sum


def square_of_sum(user_input):
    sum = 0

    for i in range(1, user_input + 1):
        sum += i

    return sum ** 2


def sum_square_difference(user_input):
    sum_of_squares_result = sum_of_squares(user_input)
    square_of_sum_result = square_of_sum(user_input)

    return square_of_sum_result - sum_of_squares_result


def main():
    user_input = get_user_input()
    print(
        f"You chose {user_input}. This means will we find the difference between the sum of the squares and the square of the sum for the first {user_input} natural numbers.")
    result = sum_square_difference(user_input)
    print(f"The difference is {result}.")


main()
