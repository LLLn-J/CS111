# Hu Xuan 7/14/2022
# xuanh@bu.edu
# Problem Set 3, Problem 2
# ps3pr2.py
# More practice writing non-recursive functions


def flipside(s):
    """ takes a string input s and returns a string
    whose first half is s‘s second half and whose second half is s‘s first half.
    """
    half_len = len(s) // 2
    return s[half_len:] + s[0:half_len]


def adjust(s, length):
    """  takes as inputs a string s and an integer length, and that returns a string
    in which the value of s has been adjusted as necessary to produce a string with
    the specified length.
    """
    if len(s) < length:
        return ' ' * (length - len(s)) + s
    else:
        return s[0:length]
