# Hu Xuan 8/10/2022
# xuanh@bu.edu
# Problem Set 11, Problem 4
# ps11pr4.py
# An AI Player

import random
from ps10pr3 import *  # to use the connect_four and process_move functions


class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ In addition to the attributes inherited from Player, an AIPlayer
        object should include two new attributes
        """
        assert (checker == 'X' or checker == 'O')
        assert (tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert (lookahead >= 0)
        Player.__init__(self, checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ returns a string representing an AIPlayer object.
        """
        return 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'

    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the board,
        and that returns the index of the column with the maximum score.
        """
        max_lst = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                max_lst += [i]

        if self.tiebreak == 'LEFT':
            return max_lst[0]
        elif self.tiebreak == 'RIGHT':
            return max_lst[-1]
        else:
            return random.choice(max_lst)

    def scores_for(self, board):
        """ takes a Board object board and determines the called
        AIPlayer‘s scores for the columns in board.
        """
        scores = [50] * board.width
        for i in range(board.width):
            if not board.can_add_to(i):
                scores[i] = -1
            elif board.is_win_for(self.checker):
                scores[i] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[i] = 0
            elif self.lookahead == 0:
                scores[i] = 50
            else:
                board.add_checker(self.checker, i)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(board)
                scores[i] = 100 - max(opp_scores)
                board.remove_checker(i)
        return scores

    def next_move(self, board):
        """ Rather than asking the user for the next move, this version of next_move
        should return the called AIPlayer‘s judgment of its best possible move.
        """
        self.num_moves += 1
        return self.max_score_column(self.scores_for(board))
