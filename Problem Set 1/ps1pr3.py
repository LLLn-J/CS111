# Hu Xuan
# xuanh@bu.edu
# Problem Set 1, Problem 3
# ps1pr3.py
# Functions with numeric inputs

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1 * x


# put your definitions for the remaining functions below

# function 1
def cube(x):
    """ takes a number x as its input
        and returns the cube of its input.
    """
    return x * x * x


# function 2
def convert_to_inches(yards, feet):
    """ takes two numeric inputs yards and feet that
        together represent a single length broken up
        into yards and feet, and that returns
        the corresponding length in inches.
    """
    return yards * 36 + feet * 12


# function 3
def area_sq_inches(height_yds, height_ft, width_yds, width_ft):
    """ takes the height and the width of a rectangle
        and return the area of the rectangle in square inches.
    """
    height_inches = convert_to_inches(height_yds, height_ft)
    width_inches = convert_to_inches(width_yds, width_ft)
    return height_inches * width_inches


# optional but encouraged: add test calls for your functions, indented below
if __name__ == '__main__':
    # sample test call for function 0
    print('opposite(-8) returns', opposite(-8))

    # sample test call for function 1
    print('cube(3) returns', cube(3))

    # sample test call for function 2
    print('convert_to_inches(1,1) returns', convert_to_inches(1, 1))

    # sample test call for function 3
    print('area_sq_inches(1,2,3,1) returns', area_sq_inches(1, 2, 3, 1))
