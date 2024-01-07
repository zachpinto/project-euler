# Problem 25
# Title: 1000-digit Fibonacci number

# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.

# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# get user input for number of digits
def get_user_digit():
    digits = int(input("Choose a number of digits: "))
    return digits


# find the index of the first term in the Fibonacci sequence to contain n digits
def find_fibonacci_index(digits):
    prev = 1
    curr = 1

    digits = 0
    index = 2

    while digits < 1000:
        prev, curr = curr, prev + curr
        digits = len(str(curr))
        index += 1

    return index, curr


# main function
def main():
    digits = get_user_digit()
    index, result = find_fibonacci_index(digits)
    print(f"The index of the first term in the Fibonacci sequence to contain {digits} digits is: {index}")


# call main function
main()
