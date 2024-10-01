#!/usr/bin/python3
"""
Prime Game Algorithm
"""


def sieve_of_eratosthenes(n):
    """
    Generates a list of prime numbers up to n using the Sieve of Eratosthenes.

    Args:
    n (int): The maximum number to check for primes.

    Returns:
    list: A list where the value at index i is True if i is a prime,
    False otherwise.
    """
    primes = [True] * (n + 1)  # Initialize all numbers as prime (True)
    primes[0], primes[1] = False, False  # 0 and 1 are not primes

    # Sieve algorithm
    for p in range(2, int(n**0.5) + 1):
        if primes[p]:
            for multiple in range(p * p, n + 1, p):
                primes[multiple] = False  # Mark multiples of p as non-prime

    return primes


def isWinner(num_rounds, nums):
    """
    Determines the winner after playing multiple rounds of the prime game.

    Maria and Ben take turns choosing a prime number and removing
    that number and its multiples from the set. The player unable
    to make a move loses the round.

    Args:
    num_rounds (int): The number of rounds to play.
    nums (list): A list of integers, where each integer represents
    the upper bound (n) for that round.

    Returns:
    str: The name of the player who won the most rounds
    ("Maria" or "Ben"), or None if there is no clear winner.
    """
    if not nums or num_rounds < 1:
        return None

    # Find the maximum value in nums to optimize the sieve computation
    max_n = max(nums)

    # Get a list of primes up to the maximum number in nums using the sieve
    primes = sieve_of_eratosthenes(max_n)

    # Create a list to count cumulative primes up to each number
    prime_counts = [0] * (max_n + 1)

    # Fill prime_counts with the cumulative number of primes up to each index
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if primes[i] else 0)

    # Track the number of wins for each player
    maria_wins = 0
    ben_wins = 0

    # Play each round and determine the winner
    for n in nums:
        # The number of primes up to n determines the winner
        if prime_counts[n] % 2 == 1:
            # Maria wins if the count of primes up to n is odd
            maria_wins += 1
        else:
            # Ben wins if the count of primes up to n is even
            ben_wins += 1

    # Determine the overall winner based on total wins
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"

    return None
