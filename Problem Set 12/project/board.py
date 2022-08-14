# Hu Xuan 8/13/2022
# xuanh@bu.edu
# Final Project
# board.py
# A Board class for the Eight Puzzle

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """

    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert (len(digitstr) == 9)
        for x in range(9):
            assert (str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.

        for r in range(3):
            for c in range(3):
                self.tiles[r][c] = int(digitstr[r * 3 + c])
                if int(digitstr[r * 3 + c]) == 0:
                    self.blank_r = r
                    self.blank_c = c

    ### Add your other method definitions below. ###
    def __repr__(self):
        """ returns a string representation of a Board object.
        """
        board = ''
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == 0:
                    board += '_ '
                else:
                    board += str(self.tiles[r][c]) + ' '
            board += '\n'
        return board

    def move_blank(self, direction):
        """ takes as input a string direction that specifies the direction
        in which the blank should move, and that attempts to modify the contents
        of the called Board object accordingly.
        """
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == 0:
                    if direction == 'left':
                        new_blank_c = c - 1
                        new_blank_r = r
                    elif direction == 'right':
                        new_blank_r = r
                        new_blank_c = c + 1
                    elif direction == 'up':
                        new_blank_r = r - 1
                        new_blank_c = c
                    elif direction == 'down':
                        new_blank_r = r + 1
                        new_blank_c = c
                    else:
                        print("unknown direction: " + direction)
                        return False
        if new_blank_r == -1 or new_blank_c == -1 or new_blank_c == 3 or new_blank_r == 3:
            return False
        else:
            temp = self.tiles[new_blank_r][new_blank_c]
            self.tiles[new_blank_r][new_blank_c] = 0
            self.tiles[self.blank_r][self.blank_c] = temp
            self.blank_r = new_blank_r
            self.blank_c = new_blank_c
            return True

    def digit_string(self):
        """ creates and returns a string of digits that corresponds to the current contents
        of the called Board object’s tiles attribute.
        """
        ans = ''
        for r in range(3):
            for c in range(3):
                ans += str(self.tiles[r][c])
        return ans

    def copy(self):
        """ returns a newly-constructed Board object that is a deep copy of the called object
        """
        new = Board(self.digit_string())
        return new

    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board object that are not
        where they should be in the goal state.
        """
        now = self.digit_string()
        goal = '012345678'
        count = 0
        for i in range(9):
            if now[i] != goal[i] and now[i] != '0':
                count += 1
        return count

    def __eq__(self, other):
        """ overloads the == operator – creating a version of the operator that works for Board objects.
        """
        return self.tiles == other.tiles
