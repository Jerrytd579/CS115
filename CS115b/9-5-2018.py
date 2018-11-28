#This is how to define the ranges of certain number sets.
#range(stop) -> [0, stop]
#   range(5) -> [0,1,2,3,4,5]

#range(start, stop) -> [start, stop)
#   range (2,5) -> [2,3,4]

#range (start, stop, step)
#   range (2, 10, 2) -> [2, 4, 6, 8]
#   range (12, 0, -3) -> (12, 9, 6, 3]

def dbl (x):
    '''returns 2 * x'''
    return 2 * x

map(dbl, [0, 1, 2, 3, 4])
# [[0, 2, 4, 6, 8] -> Map returns a new list after given a function and a list of numbers

def add(a, b):
    '''returns a + b'''
    return a + b

