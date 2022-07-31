# Hu Xuan 7/24/2022
# xuanh@bu.edu
# Problem Set 6, Problem 4
# ps6pr4.py
# Creating sequences with loops

def double(s):
    """ takes an arbitrary string s as input, and that uses a
    loop to construct and return the string formed by doubling
    each character in the string.
    """
    result = ''
    for c in s:
        result += c * 2
    return result


def weave(s1, s2):
    """  takes as inputs two strings s1 and s2 and uses a loop to
    construct and return a new string that is formed by “weaving”
    together the characters in the strings s1 and s2 to create a single string.
    """
    result = ''
    len_shorter = min(len(s1), len(s2))

    for i in range(len_shorter):
        result = result + s1[i] + s2[i]
    if len(s1) < len(s2):
        result += s2[len(s1):]
    else:
        result += s1[len(s2):]
    return result


def square_evens(values):
    """ takes a list of integers called values, and that modifies
    the list so that all of its even elements are replaced with
    their squares, but all of its odd elements are left unchanged.
    """
    for i in range(len(values)):
        if values[i] % 2 == 0:
            values[i] = values[i] ** 2


def index(elem, seq):
    """ takes as inputs an element elem and a sequence seq, and that
    uses a loop to find and return the index of the first occurrence
    of elem in seq.
    """
    for i in range(len(seq)):
        if seq[i] == elem:
            return i
    return -1
