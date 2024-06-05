"""
Problem 74: Digit factorial chains

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

def user_input():
    limit = int(input("Please choose a limit: "))
    non_repeat_chain = int(input("Please choose a number of non-repeating terms: "))
    return limit, non_repeat_chain


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def digit_factorial_sum(n):
    n = str(n)
    sum = 0
    for char in n:
        sum += factorial(int(char))
    return sum


def digit_factorial_chains(limit, non_repeat_chain):
    count = 0
    for i in range(1, limit):
        num = i
        chain = [num]
        while True:
            num = digit_factorial_sum(num)
            if num in chain:
                break
            chain.append(num)
        if len(chain) == non_repeat_chain:
            count += 1
    return count


def main():
    limit, non_repeat_chain = user_input()
    result = digit_factorial_chains(limit, non_repeat_chain)
    print(result)


main()
