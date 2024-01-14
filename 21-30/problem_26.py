# Problem 26
# Title: Reciprocal cycles

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2 = 0.5
# 1/3 = 0.(3)
# 1/4 = 0.25
# 1/5 = 0.2
# 1/6 = 0.1(6)
# 1/7 = 0.(142857)
# 1/8 = 0.125
# 1/9 = 0.(1)
# 1/10 = 0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def user_input():
    n = int(input("Give a number n such that we will find the longest recurring cycle from 1/1 through 1/(n-1): "))
    return n


def reciprocal_cycles(n):
    def cycle_length(d):
        remainders = {}
        value = 1
        position = 0

        while value != 0:
            if value in remainders:
                return position - remainders[value]
            remainders[value] = position
            value = (value % d) * 10
            position += 1

        return 0

    best_i = 0
    longest_cycle = 0

    for i in range(1, n):
        current_cycle = cycle_length(i)
        if current_cycle > longest_cycle:
            best_i = i
            longest_cycle = current_cycle

    return best_i


def main():
    n = user_input()
    result = reciprocal_cycles(n)
    print(result)


main()

