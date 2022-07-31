# Hu Xuan 7/14/2022
# xuanh@bu.edu
# Problem Set 3, Problem 3
# ps3pr3.py
# Fun with recursion, part I

def double(s):
    """  takes an arbitrary string s as input, and that uses
    recursion to construct and return the string formed by
    doubling each character in the string.
    """
    if s == '':
        return ''
    else:
        return s[0] * 2 + double(s[1:])


def copy(s, n):
    """  takes as inputs a string s and an integer n, and that uses
    recursion to create and return a string in which n copies of s
    have been concatenated together.
    """
    if n <= 0:
        return ''
    else:
        return s + copy(s, n - 1)


def compare(list1, list2):
    """ takes as inputs two lists of numbers, list1 and list2, and that
    uses recursion to compute and return the number of values in list1
    that are smaller than their corresponding value in list2.
    """
    if list1 == [] or list2 == []:
        return 0
    else:
        if list1[0] < list2[0]:
            return 1 + compare(list1[1:], list2[1:])
        else:
            return compare(list1[1:], list2[1:])
