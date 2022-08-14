# Hu Xuan 8/10/2022
# xuanh@bu.edu
# Problem Set 11, Problem 1
# ps11pr1.py
# A Holiday class

from ps9pr1 import Date


class Holiday(Date):
    def __init__(self, month, day, year, name):
        """ initialize the Holiday object.
        """
        super().__init__(month, day, year)
        self.name = name

    def __repr__(self):
        """ returns a string representation of a Holiday object.
        """
        return self.name + ' (' + super().__repr__() + ')'
