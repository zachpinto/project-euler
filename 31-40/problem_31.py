# Problem 31

# Title: Coin sums

# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

# It is possible to make £2 in the following way:

# 1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

# How many different ways can £2 be made using any number of coins?

# get user input for the target amount

def user_input():
    amount = float(input("Please choose an amount: "))  # Accept the amount as a float
    coins_str = input("Please choose a list of coin values in decimal format (e.g., .01, .02, .05): ")
    coins = [float(coin) for coin in coins_str.split(',')]  # Accept coins directly as floats

    return amount, coins

def number_ways_to_get_amount_from_coins(amount, coins):
    # Convert amounts to pence to use integer arithmetic
    amount = int(amount * 100)
    coins = [int(coin * 100) for coin in coins]

    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]

def main():
    amount, coins = user_input()
    result = number_ways_to_get_amount_from_coins(amount, coins)
    print(f"The number of ways to make the amount using the given coins is: {result}")

main()
