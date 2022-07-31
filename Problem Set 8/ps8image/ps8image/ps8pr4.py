# Hu Xuan 7/29/2022
# xuanh@bu.edu
# Problem Set 8, Problem 4
# ps8pr4.py
# Image processing, continued

from cs111png import *


def flip_vert(filename):
    """ loads the PNG image file with the specified filename and creates
    a new image in which the original image is “flipped” vertically.
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    new_img = Image(height, width)  # create a new, blank

    for r in range(height):
        for c in range(width):
            rgb = img.get_pixel(r, c)
            new_img.set_pixel(height - 1 - r, c, rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'flipv_' + filename
    new_img.save(new_filename)


def mirror_vert(filename):
    """  loads the PNG image file with the specified filename and creates
    a new image in which the original image is “mirrored” vertically.
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    for r in range(height // 2):
        for c in range(width):
            rgb = img.get_pixel(r, c)
            img.set_pixel(height - 1 - r, c, rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'mirrorv_' + filename
    img.save(new_filename)


def reduce(filename):
    """ loads the PNG image file with the specified filename and creates
    a new image that is half the size of the original image.
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    new_img = Image(height // 2, width // 2)  # create a new, blank

    for r in range(height):
        for c in range(width):
            if r % 2 == 1 or c % 2 == 1:
                rgb = img.get_pixel(r, c)
                new_img.set_pixel(r // 2, c // 2, rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'reduce_' + filename
    new_img.save(new_filename)


def extract(filename, rmin, rmax, cmin, cmax):
    """ loads the PNG image file with the specified filename and extracts
    a portion of the original image that is specified by the other four parameters.
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    new_img = Image(rmax - rmin, cmax - cmin)  # create a new, blank

    for r in range(rmin, rmax):
        for c in range(cmin, cmax):
            rgb = img.get_pixel(r, c)
            new_img.set_pixel(r - rmin, c - cmin, rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'extract_' + filename
    new_img.save(new_filename)
