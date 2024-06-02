# Problem 62

# Cubic permutations

# The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

# Find the smallest cube for which exactly five permutations of its digits are cube.

def create_cubes(limit):
    cubes = {}
    for i in range(limit):
        cube = i ** 3
        key = ''.join(sorted(str(cube)))
        if key in cubes:
            cubes[key].append(cube)
        else:
            cubes[key] = [cube]
    return cubes

def find_smallest_cube_with_permutations(cubes):
    for cube_list in cubes.values():
        if len(cube_list) == 5:
            return min(cube_list)
    return None

def main():
    limit = 10000  # Adjust this limit as needed
    cubes = create_cubes(limit)
    result = find_smallest_cube_with_permutations(cubes)
    return result

main()
