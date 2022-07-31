# Hu Xuan 7/7/2022
# xuanh@bu.edu
# Problem Set 2, Problem 2
# ps2pr2.py
# Functions on strings and lists, part I

# function 1
def first_and_last(values):
    """ takes a list values and returns a new list
    containing the first value of the original list
    followed by the last value of the original list.
    """
    first = values[0]
    last = values[-1]
    # print([first, last])
    return [first, last]


# function 2
def longer_len(s1, s2):
    """ takes as inputs two string values s1 and s2,
    and that returns the length of the longer string.
    """
    if len(s1) >= len(s2):
        return len(s1)
    else:
        return len(s2)

# print(longer_len('begin', 'on'))


# function 3
def move_to_end(s, n):
    """ takes as inputs a string value s and an integer n,
     and that returns a new string in which the first n
     characters of s have been moved to the end of the string.
    """
    return s[n:] + s[0:n]

# print(move_to_end('computer', 3))
