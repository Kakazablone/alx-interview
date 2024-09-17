#!/usr/bin/python3
"""Making change using dynamic programming"""

def makeChange(coins, total):
    """Determine the fewest number of coins needed to make up the given total."""
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins for each amount up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make total of 0

    # Sort coins to start with larger denominations
    coins.sort(reverse=True)

    # Compute the minimum coins required for each amount up to total
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, it means it's not possible to make that amount
    return dp[total] if dp[total] != float('inf') else -1

if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))  # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
