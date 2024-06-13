"""
Problem 75: Singular integer right triangles

It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3, 4, 5)
24 cm: (6, 8, 10)
30 cm: (5, 12, 13)
36 cm: (9, 12, 15)
40 cm: (8, 15, 17)
48 cm: (12, 16, 20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
"""

from math import gcd

def user_input():
    limit = int(input("Enter the limit: "))
    return limit


def count_right_angle_triangles(limit):
    perimeter_counts = {}
    max_perimeter = limit
    m = 2

    while True:
        for n in range(1, m):
            if (m - n) % 2 == 1 and gcd(m, n) == 1:
                perimeter = 2 * m * (m + n)
                if perimeter > max_perimeter:
                    break

                for p in range(perimeter, max_perimeter + 1, perimeter):
                    if p in perimeter_counts:
                        perimeter_counts[p] += 1
                    else:
                        perimeter_counts[p] = 1
        m += 1
        if m * m > max_perimeter:
            break

    count = 0
    for p in perimeter_counts.values():
        if p == 1:
            count += 1
    return count


def main():
    limit = user_input()
    result = count_right_angle_triangles(limit)
    print(f"The number of values of L ≤ {limit} for which exactly one integer sided right angle triangle can be formed is {result}")


main()
