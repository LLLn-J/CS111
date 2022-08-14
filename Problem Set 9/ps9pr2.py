# Hu Xuan 8/4/2022
# xuanh@bu.edu
# Problem Set 9, Problem 2
# ps9pr2.py
# Date clients

from ps9pr1 import Date


def get_age_on(birthday, other):
    """ accepts two Date objects as parameters: one to represent a
    person’s birthday, and one to represent an arbitrary date.
    """
    age = other.year - birthday.year
    this_year_birthday = Date(birthday.month, birthday.day, other.year)
    if this_year_birthday.is_after(other):
        age -= 1
    return age


def print_birthdays(filename):
    """ accepts a string filename as a parameter. The function should
    then open the file that corresponds to that filename, read through
    the file, and print some information derived from that file.
    """
    f = open(filename, 'r')
    for line in f.readlines():
        line = line[:-1]
        elem = line.split(',')
        name = elem[0]
        birth = Date(int(elem[1]), int(elem[2]), int(elem[3]))
        print(name + ' (' + str(birth) + ') (' + birth.day_name()+')')
    f.close()
