# Problem 19
# Counting Sundays

# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September, April, June, and November.
# All the rest have thirty-one, saving February alone, which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def counting_sundays():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day = 1
    sundays = 0

    for year in range(1900, 2001):
        for month in range(12):
            if year > 1900 and day == 6:
                sundays += 1

            if month == 1 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                day += 1

            day += months[month] % 7

            if day > 6:
                day -= 7

    return sundays


def main():
    result = counting_sundays()
    print(f"The number of Sundays that fell on the first of the month during the twentieth century is {result}.")


main()
