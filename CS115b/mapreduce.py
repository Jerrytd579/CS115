# The idea behind this is
#
#
#
#
#

from cs115 import map, reduce, range

def span(lst):
    """Returns the difference between the maximum and the minimum numbers in a list"""
    return reduce(max, lst) - reduce(min, lst)

def mult(x, y):
    """Returns the product of x and y"""
    return x * y

def add(a,b):
    """Returns the sum of a and b"""
    return a + b

def gauss(n):
    """Takes as input a positive integer n and returns the sum 1 + 2 + 3 +... + n"""
    return reduce(add, range(1, n + 1))

def sqr(x):
    """Returns the square of x"""
    return x * x

def sum_of_squares(n):
    """Takes as input a positive integer n and returns the sum 1^2 + 2^2 + 3^2.... + n^2"""
    return reduce(add, map(sqr, range(1, n + 1)))

print(gauss(10))
print (sum_of_squares(10))


# print(span([3, 1, 42, 7]))
#print(span([42, 42, 42, 42]))


list_of_ints = [1, 2, 3, 4, 5]
print(reduce(mult, list_of_ints))

list_of_strings = ['hello', 'my', 'name', 'is', 'brian']
print(reduce(max, map(len, list_of_strings)))