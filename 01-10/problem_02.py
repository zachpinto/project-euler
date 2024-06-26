# Problem 2
# Even Fibonacci numbers

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed n, find the sum of the even-valued terms.

def get_user_input():
    try:
        user_input = int(input("Enter a number: "))
        return user_input
    except ValueError:
        print("Please enter a valid number")
        return get_user_input()


def fibonacci_sequence(user_input):
    fib_sequence = [1, 2]

    while fib_sequence[-1] < user_input:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence


def sum_of_even_fibonacci_numbers(fib_sequence):
    sum = 0

    for i in fib_sequence:
        if i % 2 == 0:
            sum += i

    return sum


def main():
    user_input = get_user_input()
    print(
        f"You chose {user_input}. This means will we find the sum of all even Fibonacci numbers that are less than {user_input}.")
    fib_sequence = fibonacci_sequence(user_input)
    result = sum_of_even_fibonacci_numbers(fib_sequence)
    print(f"The sum is {result}.")


main()
