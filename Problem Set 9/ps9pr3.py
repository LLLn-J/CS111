# Hu Xuan 8/4/2022
# xuanh@bu.edu
# Problem Set 9, Problem 3
# ps9pr3.py
# Another Date client: using the dict object

# this import statement will allow you to use the Date class from ps9pr1.py
from ps9pr1 import Date


def nye_counts(start, end):
    """ counts how many times New Year’s Eve (December 31st) falls on each
    day of the week between the years start and end, inclusive of both endpoints,
    and that returns a dictionary containing those counts.
    """
    d = {}  # create an empty dictionary
    # add your code here
    d = {'Wednesday': 0, 'Saturday': 0, 'Friday': 0, 'Thursday': 0, 'Tuesday': 0, 'Sunday': 0, 'Monday': 0}
    for year in range(start, end + 1):
        eve = Date(12, 31, year)
        name = eve.day_name()
        if name in d:
            d[name] += 1
        else:
            d[name] = 1

    return d
