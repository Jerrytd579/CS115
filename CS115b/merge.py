

def num_matches(list1, list2):
    """ Return the number of elements that the two lists have in common """
    list1.sort()
    list2.sort()
    matches = i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches

def keep_matches(list1, list2):
    """ Returns a list of the elements that the two lists hawe in common. """
    list1.sort()
    list2.sort()
    i = j = 0
    result = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return result

def drop_matches(list1, list2):
    """ Returns a new list that contains only the elements in list2 that are not in list1"""
    list1.sort()
    list2.sort()
    i = j = 0
    result = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            result.append(list2[j])
            j += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1
    return result

A = [2, 3, 4, 5, 11, 23, 19]
B = [11, 23, 19, 25, 40]

print(num_matches(A, B))
print(keep_matches(A, B))
print(drop_matches(A, B))
