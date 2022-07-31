# Hu Xuan 7/24/2022
# xuanh@bu.edu
# Problem Set 6, Problem 3
# ps6pr3.py
# Estimating pi

import random
import math


def throw_dart():
    """ Simulates the throwing of a random dart at a 2 x 2 square that.
        is centered on the origin. Returns True if the dart hits a circle
        inscribed in the square, and False if the dart misses the circle.
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x ** 2 + y ** 2 <= 1.0:
        return True
    else:
        return False


### PUT YOUR WORK FOR PROBLEM 3 BELOW. ###

def for_pi(n):
    """ takes a positive integer n and returns an estimate
    of π that is based on n randomly thrown darts.
    """
    in_circle = 0
    for i in range(n):
        if throw_dart():
            in_circle += 1
        print(in_circle, "hits out of", i + 1, "throws so that pi is", (in_circle * 4.0 / (i+1)))
    return in_circle * 4.0 / n


def while_pi(error):
    """ takes a positive floating-point input error and
    returns the number of dart throws needed to produce
    an estimate of π that is less than error away from
    the “actual” value of π
    """
    est_pi = 0
    in_circle = 0
    throws = 0
    while abs(est_pi-math.pi) > error:
        if throw_dart():
            in_circle += 1
        throws += 1
        print(in_circle, "hits out of", throws, "throws so that pi is", (in_circle * 4.0 / throws))
        est_pi = in_circle * 4.0 / throws
    return throws
