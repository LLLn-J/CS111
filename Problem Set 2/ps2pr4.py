# Hu Xuan 7/8/2022
# xuanh@bu.edu
# Problem Set 2, Problem 4
# ps2pr4.py
# Functions on strings and lists, part II

def mirror(s):
    """ takes as input a string s and returns a mirrored version
    of s that is twice the length of the original string.
    """
    return s + s[-1::-1]


def is_mirror(s):
    """ takes as input a string s and returns True if s is a mirrored string. """
    return s == mirror(s[0:len(s)//2])


def replace_end(values, new_end_vals):
    """ takes as inputs a list values and another list new_end_vals,
    and that returns a new list in which the elements in new_end_vals
    have replaced the last n elements of the list values, where n is the length of new_end_vals.
    """
    return values[0:-len(new_end_vals)] + new_end_vals


def repeat_elem(values, index, num_times):
    """  takes as inputs a list values, an integer index (which you may assume is a valid index for
    one of the elements in values), and a positive integer num_times, and that returns a new list in
    which the element of values at position index has been repeated num_times times.
    """
    return values[0:index]+[values[index]]*num_times+values[index+1:]


if __name__ == '__main__':
    # test mirror function
    print(mirror('XYZ'))
    print(mirror('bacon'))

    # test is_mirror function
    print(is_mirror('baconnoca'))
    print(is_mirror('baconnocab'))

    # test replace_end function
    print(replace_end([1, 2, 3, 4, 5], [12]))
    print(replace_end([1, 2, 3, 4, 5], [10, 11]))
    print(replace_end([1, 2, 3, 4, 5], [7, 8, 9]))
    print(replace_end([0, 2, 4, 6], [4, 3, 2, 1]))      # special case 1
    print(replace_end([0, 2, 4, 6], [4, 3, 2, 1, 0]))   # special case 2

    # test repeat_elem function
    print(repeat_elem([10, 11, 12, 13], 2, 4))
    print(repeat_elem([5, 6, 7], 1, 3))

