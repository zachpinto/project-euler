"""
Problem 76: Counting summations

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

def user_input():
    number = int(input("Enter the number: "))
    return number


def count_summations(number):
    ways = [0] * (number + 1)
    ways[0] = 1

    for i in range(1, number):
        for j in range(i, number + 1):
            ways[j] += ways[j - i]

    return ways[number]


def main():
    number = user_input()
    result = count_summations(number)
    print(f"The number of ways {number} can be written as a sum of at least two positive integers is {result}")


main()
