"""
Problem 92

Square digit chains

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

def user_input():
    limit = int(input("Please choose a number, that up to it, we calculate how many numbers arrive at 89 via square digit chains: "))
    return limit

def square_digit_next(n):
    n = str(n)
    next = 0
    for char in n:
        char = int(char)
        square = char ** 2
        next += square
    return next

def main():
    count = 0
    limit = user_input()
    for i in range(1, limit):
        num = i
        while num != 1 and num != 89:
            num = square_digit_next(num)
        if num == 89:
            count += 1
    return count

main()
