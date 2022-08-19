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
        if state.creates_cycle():
            return False
        if state.num_moves > self.depth_limit and self.depth_limit != -1:
            return False
        return True

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
        self.add_state(init_state)
        while self.states != []:
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal():
                return s
            else:
                self.add_states(s.generate_successors())

        return None


### Add your BFSeacher and DFSearcher class definitions below. ###

class BFSearcher(Searcher):
    def next_state(self):
        """ Rather than choosing at random from the list of untested states, this
        version of next_state should follow FIFO (first-in first-out) ordering
        """
        s = self.states[0]
        self.states.remove(s)

        return s


class DFSearcher(Searcher):
    def next_state(self):
        """  The necessary steps are very similar to the ones that you took for BFSearcher,
        but the next_state() method should follow LIFO (last-in first-out) ordering – choosing
        the state that was most recently added to the list.
        """
        s = self.states[-1]
        self.states.remove(s)

        return s


def h0(state):
    """ a heuristic function that always returns 0 """
    return 0


def h1(state):
    """ a heuristic function that always returns 1 """
    return state.board.num_misplaced()

### Add your other heuristic functions here. ###


class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """

    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, depth_limit, heuristic):
        """ constructor for a GreedySearcher object
            inputs:
             * depth_limit - the depth limit of the searcher
             * heuristic - a reference to the function that should be used
             when computing the priority of a state
        """
        # add code that calls the superclass constructor
        super(GreedySearcher, self).__init__(depth_limit)
        self.heuristic = heuristic

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

    def priority(self, state):
        """ takes a State object called state, and that computes and returns the priority of that state.
        """
        priority = -1 * self.heuristic(state)
        return priority

    def add_state(self, state):
        """ Rather than simply adding the specified state to the list of untested states, the method
         should add a sublist that is a [priority, state] pair, where priority is the priority of state,
          as determined by calling the priority method.
        """
        self.states += [[self.priority(state), state]]

    def next_state(self):
        """ This version of next_state should choose one of the states with the highest priority. """
        s = max(self.states)
        self.states.remove(s)

        return s[1]


### Add your AStarSeacher class definition below. ###

class AStarSearcher(GreedySearcher):
    def priority(self, state):
        """ takes a State object called state, and that computes and returns the priority of that state.
        """
        priority = -1 * (self.heuristic(state) + state.num_moves)
        return priority


b = Board('142358607')
s = State(b, None, 'init')
a = AStarSearcher(-1, h1)
a.add_state(s)
succ = s.generate_successors()
a.add_state(succ[1])
