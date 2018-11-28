# Created on Sep 8, 2018
#
# I pledge my honor that I have abided by the Stevens honor system.
# @author Jerry Cheng
# jcheng15
#

from cs115 import map, reduce, range
import math


def mult(x, y):
    """Returns the product of x and y"""
    return x * y


############################################################

def factorial(n):
    """Returns the factorial of a list of numbers, n"""
    return reduce(mult, (range(1, (math.fabs(n)) + 1)))


############################################################

def add(x, y):
    """Returns the sum of x and y"""
    return x + y


def mean(L):
    """Returns the mean of given list L"""
    return reduce(add, (L)) / (len(L))

print(mean([1,2,3,4]))
############################################################

def divides(n):
    """Returns a boolean value of whether or not the remainder of n / k is equal to 0"""
    def div(k):
        return n % k == 0

    return div

print(divides(6)(2))

def prime(n):
    """Takes a positive integer, n, and returns True if n is prime, False if composite """
    if n <= 1:
        return False
    return sum(map(divides(n), (range(2, int(math.sqrt(n) + 1))))) == 0

print(map(prime, (range(0, 20))))


