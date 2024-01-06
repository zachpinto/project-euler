# Problem 23
# Non-abundant sums

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.

# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means
# that 28 is a perfect number. A number n is called deficient if the sum of its proper divisors is less than n and
# it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be
# written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all
# integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper
# limit cannot be reduced any further by analysis even though it is known that the greatest number that
# cannot be expressed as the sum of two abundant numbers is less than this limit.
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def perfect_abundant_deficient(n):
    divisor_sum = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            divisor_sum += i

    if divisor_sum == n:
        return "Perfect"
    elif divisor_sum > n:
        return "Abundant"
    else:
        return "Deficient"

def sum_ints_not_sum_of_two_abundants():
    # Finding all abundant numbers up to 28123
    abundants = [i for i in range(12, 28124) if perfect_abundant_deficient(i) == "Abundant"]
    abundant_sums = set()
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            sum_ab = abundants[i] + abundants[j]
            if sum_ab <= 28123:
                abundant_sums.add(sum_ab)

    # Summing all numbers not expressible as the sum of two abundant numbers
    total_sum = sum(i for i in range(1, 28124) if i not in abundant_sums)
    return total_sum

def main():
    result = sum_ints_not_sum_of_two_abundants()
    return result

main()
