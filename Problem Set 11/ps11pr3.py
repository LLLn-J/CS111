# Hu Xuan 8/10/2022
# xuanh@bu.edu
# Problem Set 11, Problem 3
# ps11pr3.py
# An Unintelligent Computerized Player

import random
from ps10pr3 import *  # to use the connect_four and process_move functions


class RandomPlayer(Player):
    def next_move(self, board):
        """ Rather than asking the user for the next move, this version of
        next_move should choose at random from the columns in the specified
        board that are not yet full, and return the index of that randomly
        selected column.
        """
        self.num_moves += 1
        can_add_col = []
        for i in range(board.width):
            if board.can_add_to(i):
                can_add_col += [i]
        return random.choice(can_add_col)
