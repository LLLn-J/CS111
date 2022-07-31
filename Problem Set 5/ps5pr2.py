# Hu Xuan 7/17/2022
# ps5pr2.py (Problem Set 5, Problem 2)
# xuanh@bu.edu
# List Comprehension

## INSTRUCTIONS: Uncomment these lines as you go, and test them at the console
#
lc1 = [x * 2 for x in range(5)]
#
#
#
#
words = ['hello', 'world', 'how', 'goes', 'it?']
lc2 = [w[1] for w in words]
#
#
#
lc3 = [word[::-1] * 2 for word in ['hello', 'bye', 'no']]
#
#
#
#
lc4 = [x ** 2 for x in range(1, 10) if x % 2 == 0]
#
#
#
#
lc5 = [c in ['b', 'u'] for c in 'bu be you']


#
#
#


## continue with writing functions below:

def powers_of(base, count):
    """  takes as inputs a number base and a positive integer count,
    and that uses a list comprehension to construct and return a
    list containing the first count powers of base, beginning
    with the 0th power.
    """
    return [base ** x for x in range(count)]


def shorter_than(n, wordlist):
    """ takes as inputs an integer n and a list of strings wordlist,
    and that uses a list comprehension to construct and return a list
    consisting of all words from wordlist that are shorter than n.
    """
    return [w for w in wordlist if len(w) < n]


if __name__ == '__main__':

    # test code below, do not modify!
    for x in ['lc1', 'lc2', 'lc3', 'lc4', 'lc5']:
        if x in dir():
            print(x + ' = ', eval(x))
