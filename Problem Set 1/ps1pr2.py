# Hu Xuan
# xuanh@bu.edu
# Problem Set 1, Problem 2
# ps1pr2.py
# Indexing and slicing puzzles


#
# List puzzles
#

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example puzzle (puzzle 0):
# Creating the list [2, 5, 9] from pi and e
answer0 = [e[0]] + pi[-2:]

# Solve puzzles 1-4 here:

# Puzzle 1:
# Creating the list [2, 7] from pi and/or e
answer1 = e[0:2]

# Puzzle 2:
# Creating the list [5, 4, 3] from pi and/or e
answer2 = pi[-2::-2]

# Puzzle 3:
# Creating the list [3, 5, 7] from pi and/or e
# Optional challenge: Do this with just three list operations
answer3 = pi[0::4] + [e[1]]

# Puzzle 4:
# Creating the list [1, 2, 3, 4, 5], from pi and/or e
# Optional challenge: Do this with just three list operations
answer4 = e[-1::-2] + pi[0:5:2]

#
# String puzzles
#

b = 'boston'
u = 'university'
t = 'terriers'

# Example puzzle (puzzle 5)
# Creating the string 'bossy'
# answer5 = b[:3] + t[-1] + u[-1]
# with 3 operations challenge
answer5 = b[:3] + u[6::3]
# Solve puzzles 5-10 here:

# Puzzle 6:
# Creating the string 'universe' (3 ops)
answer6 = u[0:7] + t[1]

# Puzzle 7:
# Creating the string 'roster' (5 ops)
answer7 = t[2] + b[1:4] + t[5:7]

# Puzzle 8:
# Creating the string 'boisterous' (8 ops)
answer8 = (b + u)[0::4] + t[0:3] + b[1] + u[0::6]

# Puzzle 9:
# Creating the string 'yesyesyes' (4 ops)
answer9 = (u[-1] + u[4:7:2]) * 3

# Puzzle 10:
# Creating the string 'trist' (3 ops)
answer10 = t[0:-2:2] + b[2:4]


# test code below, do not modify!
if __name__ == '__main__':

    for x in ['answer0', 'answer1', 'answer2', 'answer3', 'answer4',
              'answer5', 'answer6', 'answer7', 'answer8', 'answer9',
              'answer10']:
        if x in dir():
            print(x + ' = ', eval(x))
