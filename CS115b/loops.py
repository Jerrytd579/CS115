'''
Created on Oct 29 2018
'''

import time, random

def map_sqr(lst):
    result = []
    for x in lst:
        result.append(x * x)
    return result


def map_sqr_lst_comprehension(lst):
    '''Assume lst is a list. Return map(sqr, lst)'''
    return [x*x for x in lst]

print(map_sqr([1, 2, 3]))
print(map_sqr_lst_comprehension([1, 2, 3]))

def find_max(lst):
    '''Returns the maximum element in the list'''
    if lst == []:
        return None
    max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val

print(find_max([1, 2, 3, 4, 5]))

def find_min_max(lst):
    '''REturns a tuple of the min and max elements in the list'''
    if lst == []:
        return None
    max_val = min_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
        elif x < min_val:
            min_val = x
    return (min_val, max_val)

print(find_min_max([1, 2, 3, 4, 5, 6, 7, 8]))


def shallow_copy(lst):
    result = []
    for x in lst:
        result.append(x)
    return result

def shallow_copy_list_comprehension(lst):
    return [x for x in lst]

x = 5
L = [1, 3, [x, 7]]
M = shallow_copy(L)

print(hex(id(x)))
print(hex(id(L[2])))
print(hex(id(M[2])))

def deep_copy(lst):
    result = []
    for x in lst:
        if type(x) is list:
            result.append(deep_copy(x))
        else:
            result.append(x)
    return result

print()
x = 5
L = [1, 3, [x, 7]]
M = deep_copy(L)
M[2][0] = 6
print(hex(id(L[2])))
print(hex(id(M[2])))

def sequential_search(key, lst):
    """ Returns the index of the key in lst, if found, and -1 otherwise"""
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

def binary_search(key, lst):
    """
    Searches the lst for key.

    Arguments:
        lst -> the sorted list to search
        key -> the value to search for

        Returns:
            The index of key in lst, or -low - 1, if the key is not present. The caller of this function
            can convert index = -low - 1 to a positive index indicating where the key would be inserted
            by using the value -index - 1
    """
    low = 0
    high = len(lst) - 1
    while high >= low:
        mid = low + (high - low) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key > lst[mid]:
            low = mid + 1
        else:
            return mid
    return -low - 1

def swap(lst, a, b):
    """ Swaps list sub a with list sub b. """
    x = lst[a]
    lst[a] = lst[b]
    lst[b] = x

def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
            if min_index != i:
                swap(lst, i, min_index)


random_list = [random.randint(1, 100000) for _ in range(20000)]
copy_list = list(random_list)

start = time.clock()
selection_sort(random_list)
print('Elapsed time: %.2f seconds' % (time.clock() - start))