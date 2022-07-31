# Hu Xuan 7/17/2022
# xuanh@bu.edu
# Problem Set 4, Problem 3
# ps4pr3.py
# Recursive operations on binary numbers


def bitwise_and(b1, b2):
    """ takes as inputs two strings b1 and b2 that represent
    binary numbers. The function should use recursion to compute
    the bitwise AND of the two numbers and return the result
    in the form of a string.
    """
    if b1 == '' and b2 == '':
        return ''
    elif b1 == '' or b2 == '':
        if b1 == '':
            return len(b2) * '0'
        else:
            return len(b1) * '0'
    else:
        rest = bitwise_and(b1[:-1], b2[:-1])
        if b1[-1] == '0' or b2[-1] == '0':
            return rest + '0'
        else:
            return rest + '1'


def add_bitwise(b1, b2):
    """ The function adds two binary numbers.
    """
    if b1 == '' or b2 == '':
        if b1 == '' and b2 == '':
            return ''
        elif b1 == '':
            return b2
        else:
            return b1
    else:
        rest = add_bitwise(b1[:-1], b2[:-1])

        if b1[-1] == '0' and b2[-1] == '0':
            return rest + '0'
        elif b1[-1] == '1' and b2[-1] == '1':
            rest = add_bitwise(rest, '1')
            return rest + '0'
        else:
            return rest + '1'
