# Problem 42

# Coded triangle numbers

# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

import string

def get_triangle_numbers(n):
    return [int(0.5 * i * (i + 1)) for i in range(1, n + 1)]

def get_word_value(word):
    return sum([string.ascii_uppercase.index(c) + 1 for c in word])

def is_triangle_word(word):
    triangle_numbers = get_triangle_numbers(100)
    word_value = get_word_value(word)
    return word_value in triangle_numbers

def main():
    # ensure you add the text file from problem source to your directory locally
    with open('0042_words.txt', 'r') as f:
        words = f.read().replace('"', '').split(',')
    count = 0
    for word in words:
        if is_triangle_word(word):
            count += 1
    print(count)


main()
