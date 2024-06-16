"""
Problem 81: Path sum: two ways

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.

[131] 673 234 103 18
[201] [96] [342] 965 150
630 803 [746] [422] 111
537 699 497 [121] 956
805 732 524 [37] [331]

Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

def read_matrix():
    with open("0081_matrix.txt") as file:
        return [[int(num) for num in line.split(",")] for line in file]


def minimal_path_sum(matrix):
    size = len(matrix)
    for i in range(size - 2, -1, -1):
        matrix[i][size - 1] += matrix[i + 1][size - 1]
        matrix[size - 1][i] += matrix[size - 1][i + 1]

    for i in range(size - 2, -1, -1):
        for j in range(size - 2, -1, -1):
            matrix[i][j] += min(matrix[i + 1][j], matrix[i][j + 1])

    return matrix[0][0]


def main():
    matrix = read_matrix()
    result = minimal_path_sum(matrix)
    print(f"The minimal path sum from the top left to the bottom right is {result}")


main()
