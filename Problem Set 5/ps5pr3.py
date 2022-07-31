# Hu Xuan 7/19/2022
# xuanh@bu.edu
# Problem Set 5, Problem 3
# ps5pr3.py
# Algorithm design

def cube_all_lc(values):
    """ takes as input a list of numbers called values,
    and that uses a list comprehension to create and
    return a list containing the cubes of the numbers
    in values.
    """
    return [x ** 3 for x in values]


def cube_all_rec(values):
    """ takes as input a list of numbers called values,
    and that uses recursion to create and return a list
    containing the cubes of the numbers in values.
    """
    if values == []:
        return []
    else:
        return [values[0] ** 3] + cube_all_rec(values[1:])


def num_larger(threshold, values):
    """ takes as inputs a number threshold and a list of
    numbers values, and that returns the number of elements
    of values that are larger than threshold.
    """
    count = [1 for x in values if x > threshold]
    return sum(count)


def num_vowels(s):
    """ returns the number of vowels in the string s
        input: s is a string of 0 or more lowercase letters
    """
    if s == '':
        return 0
    else:
        num_in_rest = num_vowels(s[1:])
        if s[0] in 'aeiou':
            return 1 + num_in_rest
        else:
            return 0 + num_in_rest


def most_consonants(words):
    """ takes a list of strings called words and
    returns the string in the list with the most consonants.
    """
    count = [[len(w) - num_vowels(w), w] for w in words]
    return max(count)[1]
