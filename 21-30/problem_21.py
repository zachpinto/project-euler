# Problem 21
# Amicable Numbers

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
# amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

def get_user_sum():
    n = int(input("Choose a number: "))
    return n


def sum_of_divisors(n):
    sum_divisors = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors


def divisors_sum_dict(upper_limit):
    divisor_sums = {}
    for i in range(1, upper_limit + 1):
        divisor_sums[i] = sum_of_divisors(i)
    return divisor_sums


def sum_amicable_numbers(divisor_sums):
    amicable_sum = 0
    for key, value in divisor_sums.items():
        if key != value and value in divisor_sums and divisor_sums[value] == key:
            amicable_sum += key
    return amicable_sum


def main():
    n = get_user_sum()
    divisor_sums = divisors_sum_dict(n)
    result = sum_amicable_numbers(divisor_sums)
    print(result)


main()
