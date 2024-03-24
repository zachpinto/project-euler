


def is_triangle(n):
    return ((8 * n + 1) ** 0.5 - 1) % 2 == 0


def is_pentagonal(n):
    return ((24 * n + 1) ** 0.5 + 1) % 6 == 0


def is_hexagonal(n):
    return ((8 * n + 1) ** 0.5 + 1) % 4 == 0


def find_next_triangle():
    found = False

    while not found:
        n = 286
        while True:
            triangle = n * (n + 1) // 2
            if is_pentagonal(triangle) and is_hexagonal(triangle):
                return triangle
            n += 1


def main():
    print(find_next_triangle())


main()
