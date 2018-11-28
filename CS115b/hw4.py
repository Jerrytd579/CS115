'''
Created on 1 October 2018
@author:   jcheng15
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 4
'''


def pascal_helper(row):
    """Helper function for pascal row"""
    if len(row) <= 1:
        return []
    return [row[0] + row[1]] + pascal_helper(row[1:])

def pascal_row(n):
    """Outputs a list of elements found in a certain row, n of Pascal's triangle"""
    if n == 0:
        return [1]
    return [1] + pascal_helper(pascal_row(n - 1)) + [1]

############################################

def pascal_triangle(n):
    """Takes input, n, and returns a list of lists containing the values of all the rows up to and including
    row n"""
    if n < 0:
        return []
    return pascal_triangle(n - 1) + [pascal_row(n)]

