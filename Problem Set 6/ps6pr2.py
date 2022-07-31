# Hu Xuan 7/24/2022
# xuanh@bu.edu
# Problem Set 6, Problem 2
# ps6pr2.py
# Practice with the definite loop

def print_squares(values):
    """  takes as a parameter a list of numbers called values,
    and uses an element-based loop to compute and print out
    the square of each value.
    """
    for x in values:
        print(x ** 2)


def print_multiples(n, m):
    """ will print out the first m multiples of the
    integer n, one per line.
    """
    for i in range(m):
        print(i * n)


def num_vowels(s):
    """ process a string s and return the number of vowels
    (letters that are in the string aeiou) in that string.
    """
    count = 0          # the return value, number of vowels
    for ch in s:
        if ch in 'aeiou':
            count += 1
    return count
