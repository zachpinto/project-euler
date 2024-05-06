# Problem 5
# Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all numbers from 1 to n?

def get_user_input():
    try:
        user_input = int(input("Enter a number: "))
        return user_input
    except ValueError:
        print("Please enter a valid number")
        return get_user_input()


def smallest_multiple(user_input):
    i = (user_input + 1)

    x = 0

    while x < user_input:
        x = 0
        for j in range(1, user_input + 1):
            if i % j == 0:
                x += 1
            else:
                i += 1

    return i


def main():
    user_input = get_user_input()
    print(
        f"You chose {user_input}. This means will we find the smallest positive number that is evenly divisible by all numbers from 1 to {user_input}.")
    result = smallest_multiple(user_input)
    print(f"The smallest positive number is {result}.")


main()
