# Problem 22
# Names Scores

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
# by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

# text = (https://projecteuler.net/resources/documents/0022_names.txt)

def create_alphabet_points():
    """Create a dictionary mapping alphabet letters to points (a=1, z=26)."""
    return {chr(i + 96): i for i in range(1, 27)}

def alphabetical_value(name, alphabet_points):
    """Calculates the alphabetical value of a name."""
    return sum(alphabet_points[char.lower()] for char in name)

def main():
    alphabet_points = create_alphabet_points()
    names.sort()  # Sort the names alphabetically

    total_score = 0
    for index, name in enumerate(names, 1):  # Start index at 1
        name_score = alphabetical_value(name, alphabet_points) * index
        total_score += name_score

    return total_score


main()
