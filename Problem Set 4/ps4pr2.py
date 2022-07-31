# Hu Xuan 7/17/2022
# xuanh@bu.edu
# Problem Set 4, Problem 2
# ps4pr2.py
# Using your conversion functions

from ps4pr1 import *


def add(b1, b2):
    """ takes as inputs two strings b1 and b2 that represent
    binary numbers. The function should compute the sum of
    the numbers, and return that sum in the form of a string
    that represents a binary number.
    """
    n1 = bin_to_dec(b1)
    n2 = bin_to_dec(b2)
    n_sum = n1 + n2
    return dec_to_bin(n_sum)  # return a binary sum


def increment(b):
    """ takes an 8-character string representation of a binary
    number and returns the next larger binary number as an
    8-character string.
    """
    if b == '11111111':
        return '00000000'
    ans = dec_to_bin(bin_to_dec(b) + 1)
    length = len(ans)
    if length < 8:
        ans = (8 - length) * '0' + ans
    return ans
