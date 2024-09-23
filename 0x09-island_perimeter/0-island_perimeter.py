#!/usr/bin/python3

""" Function to calculate the perimeter of an island in a grid. """


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Parameters:
    grid (list of list of int): A 2D grid where 0 represents water and 1 represents land.

    Returns:
    int: The perimeter of the island. The perimeter is calculated by checking
         the number of edges of land cells that are adjacent to water cells or
         the grid boundary.
    """
    perimeter = 0
    num_rows = len(grid)
    num_cols = len(grid[0]) if num_rows > 0 else 0

    for row in range(num_rows):
        for col in range(num_cols):
            # Check if the current cell is land
            if grid[row][col] == 1:
                # Check each direction (up, down, left, right)
                if row == 0 or grid[row - 1][col] == 0:  # Up
                    perimeter += 1
                if row == num_rows - 1 or grid[row + 1][col] == 0:  # Down
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:  # Left
                    perimeter += 1
                if col == num_cols - 1 or grid[row][col + 1] == 0:  # Right
                    perimeter += 1

    return perimeter
