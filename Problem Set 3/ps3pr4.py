# Hu Xuan 7/14/2022
# xuanh@bu.edu
# Problem Set 3, Problem 4
# ps3pr4.py
# Fun with recursion, part II

def letter_score(letter):
    """ takes a lowercase letter as input and returns
    the value of that letter as a scrabble tile.
    """
    assert (len(letter) == 1)
    if letter in ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 'u', 't']:  # letters with a score of 1
        return 1
    elif letter in ['d', 'g']:  # letters with a score of 2
        return 2
    elif letter in ['b', 'c', 'm', 'p']:  # letters with a score of 3
        return 3
    elif letter in ['f', 'h', 'v', 'w', 'y']:  # letters with a score of 4
        return 4
    elif letter == 'k':
        return 5
    elif letter in ['j', 'x']:
        return 8
    elif letter in ['q', 'z']:
        return 10
    else:
        return 0


def scrabble_score(word):
    """ takes as input a string word containing only lowercase letters,
    and that uses recursion to compute and return the scrabble score of that string.
    """
    if word == '':
        return 0
    else:
        return letter_score(word[0]) + scrabble_score(word[1:])


def add(vals1, vals2):
    """ takes as inputs two lists of 0 or more numbers, vals1 and
    vals2, and that uses recursion to construct and return a new
    list in which each element is the sum of the corresponding
    elements of vals1 and vals2.
    """
    if vals1 == [] or vals2 == []:
        return []
    else:
        return [vals1[0] + vals2[0]] + add(vals1[1:], vals2[1:])


def weave(s1, s2):
    """  takes as inputs two strings s1 and s2 and uses recursion
    to construct and return a new string that is formed by “weaving”
    together the characters in the strings s1 and s2 to create a single string.
    """
    if s1 == '' and s2 == '':
        return ''
    elif s1 == '':
        return s2
    elif s2 == '':
        return s1
    else:
        return s1[0] + s2[0] + weave(s1[1:], s2[1:])
