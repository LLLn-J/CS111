# Hu Xuan 7/27/2022
# xuanh@bu.edu
# Problem Set 7, Problem 1
# ps7pr1.py
# 2-D lists

import random


def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []

    for r in range(height):
        row = [0] * width  # a row containing width 0s
        grid += [row]

    return grid


def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line, and nothing between values.
        input: grid is a 2-D list. We assume that all the cell
               values are integers between 0 and 9.
    """
    height = len(grid)
    width = len(grid[0])

    for r in range(height):
        for c in range(width):
            print(grid[r][c], end='')  # print nothing between values
        print()  # at end of row, go to next line


def diagonal_grid(height, width):
    """ creates and returns a height x width grid in which the cells
        on the diagonal are set to 1, and all other cells are 0.
        inputs: height and width are non-negative integers
    """
    grid = create_grid(height, width)  # initially all 0s

    for r in range(height):
        for c in range(width):
            if r == c:
                grid[r][c] = 1

    return grid


def inner_grid(height, width):
    """ creates and returns a 2-D list of height rows and width
    columns in which the “inner” cells are all 1 and the cells
    on the outer border are all 0.
    """
    grid = create_grid(height, width)
    for row in range(height):
        for col in range(width):
            if row == 0 or col == 0 or row == height - 1 or col == width - 1:
                grid[row][col] = 0
            else:
                grid[row][col] = 1
    return grid


def random_grid(height, width):
    """ creates and returns a 2-D list of height rows and width columns
    in which the inner cells are randomly assigned either 0 or 1, but the
    cells on the outer border are all 0.
    """
    grid = create_grid(height, width)
    for row in range(height):
        for col in range(width):
            if row == 0 or col == 0 or row == height - 1 or col == width - 1:
                grid[row][col] = 0
            else:
                grid[row][col] = random.choice([0, 1])
    return grid


def copy(grid):
    """ creates and returns a deep copy of grid–a new, separate 2-D list
    that has the same dimensions and cell values as grid.
    """
    height = len(grid)
    width = len(grid[0])
    same_grid = create_grid(height, width)
    for row in range(height):
        for col in range(width):
            same_grid[row][col] = grid[row][col]
    return same_grid


def invert(grid):
    """ takes an existing 2-D list of 0s and 1s and inverts it –
    changing all 0 values to 1, and changing all 1 values to 0.
    """
    height = len(grid)
    width = len(grid[0])
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 1:
                grid[row][col] = 0
            else:
                grid[row][col] = 1
