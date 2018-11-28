# Created on Sep 5, 2018
#
# I pledge my honor that I have abided by the Stevens honor system.
# @author Jerry Cheng
# jcheng15
#

from cs115 import map, range
import math


######################################################

def inverse(n):
    """Calculates the inverse of number n, and returns a floating point number, regardless if 'n' is an integer"""
    return 1.0 / n


######################################################

def factorial(x):
    """Returns the factorial of a list of numbers"""
    return math.factorial(x)


def add(x, y):
    """Returns the sum of x and y"""
    return x + y


def e(n):
    """Approximates the mathematical value 'e' using a Taylor expansion (1 + 1/1! + 1/2! + 1/3..."""
    return add((sum(map(inverse, map(factorial, range(1, n + 1))))), 1)


#######################################################


def error(n):
    """This calculates the amount of error using the given equation in the lab, math.e - e(n) """
    return abs((math.e - e(n)))



