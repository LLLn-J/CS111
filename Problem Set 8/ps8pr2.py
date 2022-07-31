# Hu Xuan 7/29/2022
# xuanh@bu.edu
# Problem Set 8, Problem 2
# ps8pr2.py
# Markov text generation

import random


def create_dictionary(filename):
    """ takes a string representing the name of a text file,
    and that returns a dictionary of key-value pairs
    """
    f = open(filename, 'r')
    dic = {}
    text = f.read()
    f.close()
    words = text.split()
    current_word = '$'
    for i in range(len(words)):
        next_word = words[i]
        if current_word in dic:
            dic[current_word] += [next_word]
        else:
            dic[current_word] = [next_word]
        if next_word[-1] == '.' or next_word[-1] == '!' or next_word[-1] == '?':
            current_word = '$'
        else:
            current_word = next_word
    return dic


def generate_text(word_dict, num_words):
    """ The function should use word_dict to generate and print num_words words.
    """
    current_word = '$'
    for i in range(num_words):
        next_list = word_dict[current_word]
        if next_list != []:
            next_word = random.choice(next_list)
            print(next_word, end=' ')
            if next_word[-1] == '.' or next_word[-1] == '!' or next_word[-1] == '?':
                next_word = '$'
        else:
            next_word = '$'
        current_word = next_word
