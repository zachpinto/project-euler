# Problem 1
# Multiples of 3 or 5

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def get_user_input():
    try:
        user_input = int(input("Enter a number: "))
        return user_input
    except ValueError:
        print("Please enter a valid number")
        return get_user_input()


def sum_of_multiples_of_3_and_5(user_input):
    sum = 0

    for i in range(1, user_input):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum


def main():
    user_input = get_user_input()
    print(
        f"You chose {user_input}. This means will we find the sum of all multiples of 3 or 5 that are less than {user_input}.")
    result = sum_of_multiples_of_3_and_5(user_input)
    print(f"The sum is {result}.")


main()