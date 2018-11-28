# Created on Sep 12, 2018
#
# I pledge my honor that I have abided by the Stevens honor system.
# @author Jerry Cheng
# jcheng15
#

##############################################################
def dot(L, K):
    """Multiplies the numbers together in a list"""
    if L == [] or K == []:
        return 0.0
    return L[0] * K[0] + dot(L[1:], K[1:])


##############################################################
def explode(S):
    """Takes a string S as input and returns a list of the characters"""
    if S == "":
        return []
    return [S[0]] + explode(S[1:])


##############################################################
def ind(e, L):
    """Takes in an element e and a sequence L and returns the index by which e is first found in L"""
    if L == [] or L == "":
        return 0
    elif e == L[0] or e == "":
        return 0
    return 1 + ind(e, L[1:])


##############################################################
def removeAll(e, L):
    """Removes all elements, e, from a list"""
    if L == []:
        return []
    if L[0] == e:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])


##############################################################
"""Takes a function, f, and filters the list through the function even(X)"""


def even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def myFilter(f, L):
    if not L:
        return L
    elif f(L[0]):
        return [L[0]] + myFilter(f, L[1:])
    else:
        return myFilter(f, L[1:])


#############################################################
"""Takes a list of numbers, L, and reverses it."""


def deepReverse(L):
    if L == []:
        return []
    if isinstance(L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]]
