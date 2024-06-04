"""
Problem 79

Passcode Derivation

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""


def passcode_derivation(x, attempts):
  while True:
    x_str = str(x)
    valid = True
    for attempt in attempts:
        attempt_str = str(attempt)
        if (attempt_str[0] in x_str and
            attempt_str[1] in x_str and
            attempt_str[2] in x_str and
            x_str.index(attempt_str[0]) < x_str.index(attempt_str[1]) < x_str.index(attempt_str[2])):
            continue
        else:
            valid = False
            break
    if valid:
        print(x_str)
        break
    x += 1


def main():
  attempts = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362, 319, 760, 316, 729, 380, 319, 728, 716]
  x = 100  # inital test value
  result = passcode_derivation(x, attempts)
  return result


main()
