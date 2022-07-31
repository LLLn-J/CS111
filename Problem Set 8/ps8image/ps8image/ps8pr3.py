# Hu Xuan 7/29/2022
# xuanh@bu.edu
# Problem Set 8, Problem 3
# ps8pr3.py
# Image processing with Image objects

from cs111png import *


def invert(filename):
    """ loads a PNG image from the file with the specified filename
        and creates a new image in which the colors of the pixels are
        inverted.
        input: filename is a string specifying the name of the PNG file
               that the function should process.
        No value is returned, but the new image is stored in a file
        whose name is invert_filename, where filename is the name of
        the original file.
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]

            # invert the colors of the pixel at row r, column c
            new_rgb = [255 - red, 255 - green, 255 - blue]
            img.set_pixel(r, c, new_rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'invert_' + filename
    img.save(new_filename)


def brightness(rgb):
    """ takes the RGB values of a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    return (21 * red + 72 * green + 7 * blue) // 100


### PUT YOUR WORK FOR PROBLEM 4 BELOW. ###

def grayscale(filename):
    """ loads the PNG image file with the specified filename, creates a new image
    that is a grayscale version of the original image, and stores it in a file
    named gray_*filename*, where *filename* is the name of the original file.
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)
            gray = brightness(rgb)

            new_rgb = [gray, gray, gray]
            img.set_pixel(r, c, new_rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'gray_' + filename
    img.save(new_filename)


def bw(filename, threshold):
    """ loads the PNG image file with the specified filename and creates a
    new image that is a black-and-white version of the original image.
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)
            bright = brightness(rgb)
            if bright > threshold:
                new_rgb = [255, 255, 255]
            else:
                new_rgb = [0, 0, 0]
            img.set_pixel(r, c, new_rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'bw_' + filename
    img.save(new_filename)


def fold_diag(filename):
    """ loads the PNG image file with the specified filename and creates
    a new image in which the original image is “folded” along its diagonal.
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            if r > c:
                new_rgb = [255, 255, 255]
                img.set_pixel(r, c, new_rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'fold_' + filename
    img.save(new_filename)
