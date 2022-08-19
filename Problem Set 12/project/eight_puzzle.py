# Hu Xuan 8/3/2022
# xuanh@bu.edu
# Final project
# eight_puzzle.py (Final Project)
# driver/test code for state-space search on Eight Puzzles


from searcher import *
from timer import *


def create_searcher(algorithm, depth_limit=-1, heuristic=None):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * depth_limit - an optional parameter that can be used to
            specify a depth limit          * heuristic - an optional parameter that can be used to pass
            in a heuristic function
            
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None

    if algorithm == 'random':
        searcher = Searcher(depth_limit)
    ## You will uncommment the following lines as you implement
    ## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(depth_limit)
    elif algorithm == 'DFS':
        searcher = DFSearcher(depth_limit)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(depth_limit, heuristic)
    elif algorithm == 'A*':
        searcher = AStarSearcher(depth_limit, heuristic)
    else:
        print('unknown algorithm:', algorithm)

    return searcher


def eight_puzzle(init_boardstr, algorithm, depth_limit=-1, heuristic=None):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * depth_limit - an optional parameter that can be used to
            specify a depth limit 
          * heuristic - an optional parameter that can be used to pass
            in a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')

    searcher = create_searcher(algorithm, depth_limit, heuristic)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()

    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()


def process_file(filename, algorithm, depth_limit=-1, heuristic=None):
    """  open the file with the specified filename for reading, and it should use a
    loop to process the file one line at a time.
    """
    f = open(filename, 'r')
    solved = 0
    count_moves = 0
    count_states = 0
    for line in f.readlines():
        line = line[:-1]

        init_board = Board(line)
        s = State(init_board, None, 'init')

        searcher = create_searcher(algorithm, depth_limit, heuristic)
        soln = None
        term = False
        try:
            soln = searcher.find_solution(s)
        except KeyboardInterrupt:
            print(line + ': search terminated, ', end='')
            term = True

        if soln == None and term == False:
            print(line + ': no solution')
        elif term == True:
            print('no solution')
        else:
            solved += 1
            print(line + ': ' + str(soln.num_moves) + ' moves, ' + str(searcher.num_tested) + ' states tested')
            count_moves += soln.num_moves
            count_states += searcher.num_tested
    print()
    if solved == 0:
        print('solved 0 puzzles')
    else:
        print('solved ' + str(solved) + ' puzzles')
        print('averages: ' + str(count_moves / solved) + ' moves, ' + str(count_states / solved) + ' states tested')
    f.close()
