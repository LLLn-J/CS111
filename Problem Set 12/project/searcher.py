# Hu Xuan 8/3/2022
# xuanh@bu.edu
# Final project
# searcher.py
# classes for objects that perform state-space search on Eight Puzzles  


import random
from state import *


class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """

    ### Add your Searcher method definitions here. ###
    def __init__(self, depth_limit):
        """ constructs a new Searcher object by initializing some attributes
        """
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit

    def should_add(self, state):
        """ takes a State object called state and returns True if the called
        Searcher should add state to its list of untested states, and False otherwise.
        """
        return not (state.num_moves > self.depth_limit and state.creates_cycle())

    def add_state(self, new_state):
        """ adds takes a single State object called new_state and adds it to the
        Searcher‘s list of untested states.
        """
        self.states += [new_state]

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s

    def add_states(self, new_states):
        """ takes a list State objects called new_states, and that
        processes the elements of new_states one at a time
        """
        for s in new_states:
            if self.should_add(s):
                self.add_state(s)

    def next_state(self):
        """ chooses the next state to be tested from the list of
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s

    def find_solution(self, init_state):
        """ performs a full random state-space search, stopping when the
        goal state is found or when the Searcher runs out of untested states.
        """


### Add your BFSeacher and DFSearcher class definitions below. ###


def h0(state):
    """ a heuristic function that always returns 0 """
    return 0


### Add your other heuristic functions here. ###


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """

    ### Add your GreedySearcher method definitions here. ###

    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s

### Add your AStarSeacher class definition below. ###
