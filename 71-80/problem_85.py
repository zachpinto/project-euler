# Problem 85

# Counting rectangles

# By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

# Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

import math


# Get user input
def user_input():
    target = int(input("Enter the input: "))
    return target


# Implementing the formula for counting rectangles
# This was found online
def count_rectangles(width, height):
    return width * (width + 1) * height * (height + 1) // 4


# for each combo of width and height, up to 99x99, calculate the number of rectangles, and record its area
# when the first count of rectangles goes over 2 million, return the area of this count or of the previous count (depending on which is closer to 2 million)
def find_nearest_solution(target):
    min_diff = target
    area = 0
    # assuming it's not going to be more than 99x99
    for width in range(1, 100):
        for height in range(1, 100):
            count = count_rectangles(width, height)
            diff = abs(count - target)
            if diff < min_diff:
                min_diff = diff
                area = width * height
    return area


def main():
    target = user_input()
    result = find_nearest_solution(target)
    print(result)


main()
