# Hu Xuan 7/27/2022
# xuanh@bu.edu
# Problem Set 7, Problem 3
# ps7pr3.py
# Images as 2-D lists

from hmcpng import *


def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels


def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
    width columns in which all of the pixels are green (i.e., have RGB
    values [0,255,0]).
    """
    return create_uniform_image(height, width, [0, 255, 0])


def flip_horiz(pixels):
    """ takes the 2-D list pixels containing pixels for an image, and
    that creates and returns a new 2-D list of pixels for an image in
    which the original image is “flipped” horizontally.
    """
    flipped = blank_image(len(pixels), len(pixels[0]))
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            flipped[r][c] = pixels[r][len(pixels[0]) - 1 - c]
    return flipped


def flip_vert(pixels):
    """ takes the 2-D list pixels containing pixels for an image, and
    that creates and returns a new 2-D list of pixels for an image in
    which the original image is “flipped” vertically.
    """
    flipped = blank_image(len(pixels), len(pixels[0]))
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            flipped[r][c] = pixels[len(pixels) - 1 - r][c]
    return flipped


def transpose(pixels):
    """ takes the 2-D list pixels containing pixels for an image, and
    that creates and returns a new 2-D list that is the transpose of pixels.
    """
    transp = blank_image(len(pixels[0]), len(pixels))
    for r in range(len(pixels[0])):
        for c in range(len(pixels)):
            transp[r][c] = pixels[c][r]
    return transp


def rotate_clockwise(pixels):
    """ rotate the original image clockwise by 90 degrees.
    """
    return flip_horiz(transpose(pixels))


def rotate_counterclockwise(pixels):
    """ rotate the original image counterclockwise by 90 degrees.
    """
    return rotate_clockwise(rotate_clockwise(rotate_clockwise(pixels)))
