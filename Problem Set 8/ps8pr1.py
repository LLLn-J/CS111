# Hu Xuan 7/29/2022
# xuanh@bu.edu
# Problem Set 8, Problem 1
# ps8pr1.py
# Using string methods


s1 = 'Three little kittens lost their mittens'
s2 = 'Star light, star bright'

# count all occurrences of the letter T (both upper-case and lower-case) in s1,
# and assign the count to the variable answer0
answer0 = s1.count('T') + s1.count('t')

# Puzzle 1
answer1 = s1.replace('tt', 'pp')

# Puzzle 2
answer2 = s2.split('r')

# Puzzle 3
answer3 = s2.upper().replace('STAR', 'NIGHT')

# Puzzle 4
answer4 = s1.lower().split('th')

# Puzzle 5
answer5 = s2.replace('ight', 'ook').split(',')

# do your work here!


# put any print statements/test code inside this controlled block:
if __name__ == '__main__':
    print('s1 =', s1)
    print('s2 =', s2)

    print('answer0 =', answer0)
    print('answer1 =', answer1)
    print('answer2 =', answer2)
    print('answer3 =', answer3)
    print('answer4 =', answer4)
    print('answer5 =', answer5)

    # optional: add your test code here
