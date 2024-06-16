"""
Problem 82: Path sum: three ways

NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and moving left, right, up, and down, is indicated in red and is equal to 994.

[131] 673 234 103 [18]
[201] [96] [342] 965 [150]
[630] [803] [746] [422] [111]
[537] [699] [497] [121] [956]
[805] [732] [524] [37] [331]

Find the minimal path sum from the left column to the right column in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

from math import inf


def read_matrix():
    with open("0081_matrix.txt") as file:
        return [[int(num) for num in line.split(",")] for line in file]


def minimal_path_sum(matrix):
    size = len(matrix)
    dp = [[inf] * size for _ in range(size)]

    # Initialize the first column with the matrix values
    for i in range(size):
        dp[i][0] = matrix[i][0]

    for j in range(1, size):
        for i in range(size):
            # Move right from the same row
            dp[i][j] = dp[i][j-1] + matrix[i][j]

        for i in range(1, size):
            # Move down
            dp[i][j] = min(dp[i][j], dp[i-1][j] + matrix[i][j])

        for i in range(size-2, -1, -1):
            # Move up
            dp[i][j] = min(dp[i][j], dp[i+1][j] + matrix[i][j])

    return min(dp[i][size-1] for i in range(size))


def main():
    matrix = read_matrix()
    result = minimal_path_sum(matrix)
    print(f"The minimal path sum from the left column to the right column is {result}")


main()
