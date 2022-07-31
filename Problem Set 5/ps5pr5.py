# Hu Xuan 7/19/2022
# xuanh@bu.edu
# Problem Set 5, Problem 5
# ps5pr5.py
# More algorithm design!


def index(elem, seq):
    """ takes as inputs an element elem and a sequence seq,
    and that uses recursion to find and return the index of
    the first occurrence of elem in seq.
    """
    if seq == []:
        return -1
    elif seq == '':
        return -1
    elif seq[0] == elem:
        return 0
    else:
        if index(elem, seq[1:]) == -1:
            return -1
        else:
            return 1 + index(elem, seq[1:])


def jscore(s1, s2):
    """ takes two strings s1 and s2 as inputs and returns
    the Jotto score of s1 compared with s2
    """
    if s1 == '':
        return 0
    else:
        if s1[0] in s2:
            s2 = rem_first(s1[0], s2)
            return 1 + jscore(s1[1:], s2)
        else:
            return jscore(s1[1:], s2)


def rem_first(elem, values):
    """ removes the first occurrence of elem from the list values
    """
    if values == '':
        return ''
    elif values[0] == elem:
        return values[1:]
    else:
        result_rest = rem_first(elem, values[1:])
        return values[0] + result_rest


def lcs(s1, s2):
    """  takes two strings s1 and s2 and returns the longest common subsequence (LCS) that they share.
    """
    if s1 == '' or s2 == '':
        return ''
    elif s1[-1] == s2[-1]:
        return lcs(s1[:-1], s2[:-1]) + s1[-1]
    else:
        result1 = lcs(s1[:-1], s2)
        result2 = lcs(s1, s2[:-1])
        if len(result1) > len(result2):
            return result1
        return result2
