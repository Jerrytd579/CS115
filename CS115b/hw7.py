'''
Created on 23 October 2018
@author:   jcheng15
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 7
'''

def numToBase(n, b):
    """ Convert a base 10 number to same number of said base """
    if n == 0:
        return "0"
    return str(int(numToBase(int(n / b), b) + str(n % b)))

def baseBToNum(s, b):
    """ Converts a number in base b to decimal format """
    if s == "":
        return 0
    return (int(s[0])) * (b ** (len(s) - 1)) + baseBToNum(s[1:], b)

def baseToBase(b1, b2, sinb1):
    """ Takes three inputs: a base B1, a base B2 (both of which are between 2 and 10, inclusive) and SinB1,
    which is a string representing a number in base B1.baseToBaseshould return a string representing the same number
    in base B2 """
    return numToBase(baseBToNum(sinb1, b1), b2)

def add(s, t):
    """ Adds two binary numbers together. It does so by first converting the numbers into decimal form,
    adding them, and returning the result. """
    return numToBase(baseBToNum(s, 2) + baseBToNum(t, 2), 2)

def addB(s, t):
    """ Adds two binary numbers together without converting back to base 10 """
    if s == "":
        return t
    if t == "":
        return s
    elif int(s[-1]) + int(t[-1]) == 1:
        return addB(s[:-1], t[:-1]) + '1'
    elif int(s[-1]) + int(t[-1]) == 0:
        return addB(s[:-1], t[:-1]) + '0'
    return helper(s[-1], t[-1], 1)+ '0'

def helper(s, t, a):
    """Helper function"""
    if t == "" or s == "":
        return 0
    if int(s[-1]) + int(t[-1] == 2):
        return "10"
    if int(s) + int(t) + 1 == 3:
        return "11"
    else:
        return "1"