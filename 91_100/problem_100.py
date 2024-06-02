# Problem 100

# Arranged probability

# If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

# The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

# By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.

def user_input():
    limit = 10 ** 12
    return limit


def find_n_blue(limit):
    blue = 3
    total = 4
    values = [(blue, total)]
    while total <= limit:
        blue, total = 3 * blue + 2 * total - 2, 4 * blue + 3 * total - 3
        values.append((blue, total))
    return values


def main():
    limit = user_input()
    values = find_n_blue(limit)
    for i, (blue, total) in enumerate(values):
        print(f"Step {i}: Blue discs = {blue}, Total discs = {total}")

    final_blue_discs = values[-1][0]
    print(f"Therefore, the number of Blue discs that satisfy the condition is {final_blue_discs:,}")


main()
