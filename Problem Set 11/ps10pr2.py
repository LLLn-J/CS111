# Hu Xuan 8/6/2022
# xuanh@bu.edu
# Problem Set 10, Problem 2
# ps10pr2.py
# A Connect Four Player class

from ps10pr1 import Board


# Write your class below.
class Player:
    def __init__(self, checker):
        """ constructs a new Player object by initializing the following two attributes
        """
        assert (checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ returns a string representing a Player object. The string returned should
        indicate which checker the Player object is using.
        """
        return 'Player ' + self.checker

    def opponent_checker(self):
        """ returns a one-character string representing the checker of the Player object’s
        opponent. The method may assume that the calling Player object has a checker attribute
        that is either 'X' or 'O'.
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, b):
        """ accepts a Board object b as a parameter and returns the column where the player wants
        to make the next move.
        """
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))
            # if valid column index, return that integer
            # else, print 'Try again!' and keep looping
            if b.can_add_to(col):
                return col
            else:
                print('Try again!')
