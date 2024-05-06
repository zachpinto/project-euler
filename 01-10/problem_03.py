# Problem 3
# Largest prime factor

# The prime factors of 13195 are 5, 7, 13, and 29.
# What is the largest prime factor of the number n?

def get_user_input():
    try:
        user_input = int(input("Enter a number: "))
        return user_input
    except ValueError:
        print("Please enter a valid number")
        return get_user_input()


def largest_prime_factor(user_input):
    i = 2

    while i * i <= user_input:
        if user_input % i:
            i += 1
        else:
            user_input //= i

    return user_input


def main():
    user_input = get_user_input()
    print(f"You chose {user_input}. This means will we find the largest prime factor of {user_input}.")
    result = largest_prime_factor(user_input)
    print(f"The largest prime factor is {result}.")


main()
