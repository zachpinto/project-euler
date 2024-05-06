# Problem 10
# Summation of primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
# Find the sum of all the primes below n

def get_user_input():
    try:
        user_input = int(input("Enter a number: "))
        return user_input
    except ValueError:
        print("Please enter a valid number")
        return get_user_input()


def sum_of_primes(user_input):
    sum = 0

    for i in range(2, user_input):
        if is_prime(i):  # is_prime function is defined in Problem 7
            sum += i

    return sum


def main():
    user_input = get_user_input()
    print(f"You chose {user_input}. This means will we find the sum of all primes below {user_input}.")
    result = sum_of_primes(user_input)
    print(f"The sum is {result}.")


main()
