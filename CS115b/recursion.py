
from cs115 import map, range, reduce, filter
import math

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def tower(n):
    """Computes 2^(2^(2....))) n times."""
    if n == 0:
        return 1
    return 2 ** tower(n - 1)


print(map(factorial, range(10)))
print(map(tower, range(6)))

def tower_reduce(n):
    """Computes 2^(2^(2....))) n times using reduce."""
    def power(a, b):
        return b ** a

    return reduce(power, [2] * n)

print(map(tower_reduce, range(1, 5)))

def length(lst):
    """Returns the length of the list"""
    if lst == []:
        return 0
    return 1 + length(lst[1:])

print (length([1 ,2, 5, 7, 8]))


def length_str(s):
    """Returns the length of the string"""
    if s == '':
        return 0
    return 1 + length_str(s[1:])


print(length_str("Stevens"))


def reverse(lst):
    """Takes as input a list of elements and returns the list in reverse order."""
    if lst == []:
        return []
    return reverse(lst[1:]) + [lst[0]]
    # return [lst[-1]] + reverse(lst[:-1])


print(reverse([1, 2, 3, 4]))


def member(x, lst):
    """Returns True if x is contained in the list and False otherwise."""
    if lst == []:
        return False
    if lst[0] == x:
        return True
    return member(x, lst[1:])


def collapse(lst):
    """Collapses a list of possibly nested lists into a single list of values"""
    if lst==[]:
        return []
    if isinstance(lst[0],list):
        return collapse(lst[0]) + collapse(lst[1:])
    return [lst[0]] + collapse(lst[1:])

x = [[1,2], 3, [4,5]]
print(collapse(x))

def my_map(f, lst):
    """Returns a new list where the function f has been applied to every element in the original list."""
    if lst == []:
        return []
    return [f(lst[0])] + my_map(f, lst[1:])

def sqr(x):
    return x * x

print(my_map(sqr, [1,2,3]))


def power(x, y):
    """Returns x^y"""
    if y == 0:
        return 1
    return x * power(x, y-1)


def power_tail(x, y):
    """Computes x^y with tail recursion"""
    def power_tail_helper(x, y, accum):
        if y == 0:
            return accum
        return power_tail_helper(x, y - 1, accum * x)
    return power_tail_helper(x, y, 1)


def my_reduce(f, lst):
    """Reduces a new list where it's been reduces to a single value as dictated by the predicate f"""
    def my_reduce_helper(f, lst, accum):
        if lst == []:
            return accum
        return my_reduce_helper(f, lst[1:], f(accum, lst[0]))
    if lst == []:
        raise TypeError('my_reduce(0 or empty sequence with no initial value')
    return my_reduce_helper(f, lst[1:], lst[0])

def add(x, y):
    return x + y

print(my_reduce(add, [1, 2, 3]))

def prime(n):
    """Returns whether or not an integer is prime"""
    possible_divisors = range(2, int(math.sqrt(n)) + 1)
    divisors = filter(lambda x: n % x == 0, possible_divisors)
    return len(divisors) == 0

def primes(n):
    def sieve(lst):
        if lst == []:
            return []
        return [lst[0]] + sieve(filter(lambda x: x % lst[0] != 0, lst[1:]))
    return sieve(range(2, n+1))

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n -2)

def subset(target, lst):
    """Determines whether or not it is possible to create target sum using the values
     in the list. Values in the list can be positive, negative, or zero."""
    if target == 0:
        return True
    if lst == []:
        return False
    return subset(target - lst[0], lst[1:]) or subset(target, lst[1:])

# def powerset(target, lst):
#     """Returns the power set of the list, that is, the set of all subsets of the list."""
#     if lst == []:
#         return [[]]
#     lose_it = powerset(lst[1:])
#     use_it = map(lambda subset: [lst[0]] + subset, lose_it)
#     return lose_it + use_it

def subset_with_values(target, lst):
    """Determines whether or not it is possible to create the target sum using values in the list.
    Values in the list can be positive, negative, or zero. The function returns a tuple of exactly
    two items. The first is a Boolean that indicates True if the sum is possible and False if it's
    not. The second element in the tuple is a list of all the values that add up to make the target sum."""

    if target == 0:
        return (True, [])
    if lst == []:
        return (False, [])
    use_it = subset_with_values(target - lst[0], lst[1:])
    if use_it[0]:
        return (True, [lst[0]] + use_it[1])
    return subset_with_values(target, lst[1:])
#
# def LCS(s1, s2):
#     """Returns the Length of the longest common subsequence in strings s1 and s2"""
#
#     if s1 == "" or s2 == "":
#         return 0
#     if s1[0] == s2[0]:
#         return 1 + LCS(s1[1:], s2[1:])
#     return LCS(s1, s2[1:]), LCS(s1[1:], s2)
#
# print(LCS('stocks', 'rocks'))
# print(LCS('stop', 'losses'))

def LCS_with_values(s1, s2):
    if s1 == "" or s2 == "":
        return[0, ""]
    if s1[0] == s2[0]:
        result = LCS_with_values(s1[1:], s2[1:])
        return[1 + result[0], s1[0] + result[1]]
    useS1 = LCS_with_values(s1, s2[1:])
    useS2 = LCS_with_values(s1[1:], s2)
    if useS1[0] > useS2[0]:
        return useS1
    return useS2

print(LCS_with_values("pole", "poke"))

def coin_row(lst):
    if lst == []:
        return 0
    return  max(lst[0] + coin_row(lst[2:]), coin_row(lst[1:]))

def coin_row_with_values(lst):
    if lst == []:
        return [0, []]
    use_it = coin_row_with_values(lst[2:])
    new_sum = lst[0] + use_it[0]
    lose_it = coin_row_with_values(lst[1:])
    if new_sum > lose_it[0]:
        return [new_sum, [lst[0]] + use_it[1]]
    return lose_it

def distance(first, second):
    if first == "":
        return len(second)
    if second == "":
        return len(first)
    if first[0] == second[0]:
        return distance(first[1:], second[1:])
    substitution = distance(first[1:], second[1:])   deletion = distance(first, second[1:])
    insertion = distance(first[1:], second)
    return 1 + min(substitution, deletion, insertion)
#
# L = ['w', 'x', 'y', 'z', 'a']
# M = [1, 2, 4, 8, 16]
# N = L[ M[1]: ]

L = ['roses', 'are', 'red', 'violets', 'are', 'blue', 'python', 'is', 'fun']
M = range( 1, len(L), 3 )
print(L[ M[2] ])
print(M)
print(range(1, len(L), 3))