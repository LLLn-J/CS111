# Hu Xuan 7/17/2022
# xuanh@bu.edu
# Problem Set 4, Problem 1
# ps4pr1.py
# From binary to decimal and back!


def dec_to_bin(n):
    """ takes a non-negative integer n and uses
    recursion to convert it from decimal to binary
    """
    if n == 1:
        return '1'
    elif n == 0:
        return '0'
    else:
        rest = dec_to_bin(n // 2)
        if n % 2 == 1:
            return rest + '1'
        else:
            return rest + '0'


def bin_to_dec(b):
    """ takes a string b that represents a binary number
    and uses recursion to convert the number from binary
    to decimal, returning the resulting integer.
    """
    if b == '1':
        return 1
    elif b == '0':
        return 0
    else:
        if b[-1] == '1':
            return 2 * bin_to_dec(b[:-1]) + 1
        else:
            return 2 * bin_to_dec(b[:-1]) + 0
