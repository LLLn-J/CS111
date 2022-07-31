# Hu Xuan
# xuanh@bu.edu
# Problem Set 1, Problem 1
# ps1pr1.py
# Computes the integers 0 through 4 using exactly 4 fours.

zero = 4 + 4 - 4 - 4
one = 4 // 4 - 4 + 4
two = 4 // 4 + 4 // 4
three = (4 + 4 + 4) // 4
four = 4 + (4 - 4) * 4

# test code below, do not modify!
if __name__ == '__main__':

    for x in ['zero', 'one', 'two', 'three', 'four']:
        if x in dir():
            print(x + ' = ', eval(x))
