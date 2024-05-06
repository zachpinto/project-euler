# Problem 7
# nth prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the nth prime number?

def get_user_input():
    try:
        user_input = int(input("Enter a number: "))
        return user_input
    except ValueError:
        print("Please enter a valid number")
        return get_user_input()


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def nth_prime(user_input):
    prime_count = 0
    i = 2

    while True:
        if is_prime(i):
            prime_count += 1

        if prime_count == user_input:
            return i

        i += 1


def main():
    user_input = get_user_input()
    print(f"You chose {user_input}. This means will we find the {user_input}th prime number.")
    result = nth_prime(user_input)
    print(f"The {user_input}th prime number is {result}.")


main()
