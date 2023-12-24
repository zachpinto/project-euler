# Problem 17
# Number letter counts

# If the snippets were to be combined, the main functions would need to be combined as well.
# The get_user_input functions would need to be combined into one function, and the count_paths_with_memo and sum_digits_power functions would need to be combined into one function.
# The combined function would need to handle both cases of calculating lattice paths and summing the digits of a power of 2.
# The main function would then call this combined function to get the final result.

num_letter_count = {
    "one": 3, "two": 3, "three": 5, "four": 4,
    "five": 4, "six": 3, "seven": 5, "eight": 5,
    "nine": 4, "ten": 3, "eleven": 6, "twelve": 6,
    "thirteen": 8, "fourteen": 8, "fifteen": 7,
    "sixteen": 7, "seventeen": 9, "eighteen": 8, "nineteen": 8,
    "twenty": 6, "thirty": 6, "forty": 5, "fifty": 5,
    "sixty": 5, "seventy": 7, "eighty": 6, "ninety": 6,
    "hundred": 7, "thousand": 8
}

def get_user_input():
    try:
        n = int(input("Please choose a number: "))
        return n
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None

def num_to_words(n):
    if n < 20:
        return num_letter_count[n]
    elif n < 100:
        tens = n // 10 * 10
        ones = n % 10
        if ones == 0:
            return num_letter_count[tens]
        else:
            return num_letter_count[tens] + num_letter_count[ones]
    elif n < 1000:
        hundreds = n // 100
        remainder = n % 100
        if remainder == 0:
            return num_letter_count[hundreds] + num_letter_count[100]
        else:
            return num_letter_count[hundreds] + num_letter_count[100] + "and" + num_to_words(remainder)
    elif n == 1000:
        return "onethousand"  # as "one thousand" without space for counting

def count_letters(n):
    total_letters = 0
    for i in range(1, n + 1):
        words = num_to_words(i)
        total_letters += len(words)
    return total_letters

def main():
    n = get_user_input()
    if n is not None:
        result = count_letters(n)
        print(f"Total number of letters from 1 to {n}: {result}")

# Dictionary of numbers to their word lengths
num_letter_count = {
    1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
    15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
    60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
    100: "hundred"
}

# Map number words to their lengths without spaces or hyphens
for key in list(num_letter_count.keys()):
    num_letter_count[key] = num_letter_count[key].replace(" ", "").replace("-", "")

main()
