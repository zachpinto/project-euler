# Problem 15
# Lattice paths

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

def get_user_input():
  try:
    n = int(input("Please choose a matrix size N for the NxN matrix: "))
    return n
  except ValueError:
    print("Invalid input. Please enter a valid integer.")
    return None


def count_paths_with_memo(n, x=0, y=0, memo=None):
    if memo is None:
        memo = {}

    # Check if the result is already in the memo dictionary
    if (x, y) in memo:
        return memo[(x, y)]

    # Base case: If at the bottom-right corner
    if x == n and y == n:
        return 1

    # Out of bounds: If the current position is outside the grid
    if x > n or y > n:
        return 0

    # Recursive call: Calculate paths by moving right and down, then store in memo
    memo[(x, y)] = count_paths_with_memo(n, x, y + 1, memo) + count_paths_with_memo(n, x + 1, y, memo)
    return memo[(x, y)]


def main():
  n = get_user_input()
  result = count_paths_with_memo(n)
  return result


main()
