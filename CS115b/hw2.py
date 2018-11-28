'''
Created on Sep 13 2018
@author:   jcheng15
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter

# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
    [['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10]]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']


# Implement your functions here.

def letterScore(letter, scorelist):
    """Takes as input a single letter string and a list in the element and gets a value from them"""
    if scorelist == []:
        return 0
    if scorelist[0][0] == letter:
        return scorelist[0][1]
    return letterScore(letter, scorelist[1:])


def wordScore(S, scorelist):
    """Takes as input a letter string and gets the score from a word string"""
    if S == "":
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)


#############################################
def list_of_words(Dict, Rack):
    return filter(lambda word: isPossible(word, Rack), Dict)


def isPossible(word, Rack):
    """Tests to see if word can be made with letters in rack"""
    if word == "":
        return True
    if word[0] in Rack:
        return isPossible(word[1:], remove(word[0], Rack))
    return False


def remove(letter, Rack):
    """Removes letter from rack"""
    if Rack == []:
        return []
    if Rack[0] == letter:
        return Rack[1:]
    return [Rack[0]] + remove(letter, Rack[1:])


##############################################
def scoreList(Rack):
    return map(lambda word: [word, wordScore(word, scrabbleScores)], list_of_words(Dictionary, Rack))

##############################################
def bestWord(Rack):
    scorelist = scoreList(Rack)
    if scorelist == []:
        return ["", 0]
    return reduce(lambda x, y: x if x[1]>y[1] else y, scorelist)

print(bestWord(["a", "s", "m", "t", "p"]))