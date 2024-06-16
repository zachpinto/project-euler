"""
Problem 83: Path sum: four ways

NOTE: This problem is a significantly more challenging version of Problem 81.

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

[131] 673 234 103 18
[201] [96] [342] 965 150
630 803 [746] [422] 111
537 699 497 [121] 956
805 732 524 [37] [331]

Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

import heapq
from math import inf


def read_matrix():
    with open("0081_matrix.txt") as file:
        return [[int(num) for num in line.split(",")] for line in file]


def minimal_path_sum(matrix):
    size = len(matrix)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    min_heap = [(matrix[0][0], 0, 0)]
    distances = [[inf] * size for _ in range(size)]
    distances[0][0] = matrix[0][0]

    while min_heap:
        current_dist, x, y = heapq.heappop(min_heap)

        if x == size - 1 and y == size - 1:
            return current_dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < size and 0 <= ny < size:
                new_dist = current_dist + matrix[nx][ny]
                if new_dist < distances[nx][ny]:
                    distances[nx][ny] = new_dist
                    heapq.heappush(min_heap, (new_dist, nx, ny))


def main():
    matrix = read_matrix()
    result = minimal_path_sum(matrix)
    print(f"The minimal path sum from the top left to the bottom right is {result}")


main()
