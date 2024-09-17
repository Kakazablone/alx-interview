#!/usr/bin/python3
"""Making change using dynamic programming"""


def makeChange(coins, total):
    """Finds the minimum number of coins to make up a given total"""
    if total <= 0:
        return 0

    # Initialize the dp array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Loop through each coin
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the result for the total
    return dp[total] if dp[total] != float('inf') else -1


if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
