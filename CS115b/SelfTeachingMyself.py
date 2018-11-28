"""

Self Teaching Myself Stuff

Includes things from CodingBat, StackOverflow, etc.


"""


def front3(str):
    """ Got this one wrong because I forgot that the list from [0:2] does not include index [2]"""
    front = str[0:3]
    return front + front + front


print(front3("Java"))


######################################################################################################
def string_bits(str):
    # Takes a string and returns every other char in that string -> Heeololeo returns Hello
    result = ""
    for x in range(len(str)):
        if x % 2 == 0:
            # Checks to see if x is an odd value - if its even result will be appended with the char. Otherwise, skips.
            result += str[x]
    return result


print(string_bits("Heeololeo"))

#######################################################################################################
"""

Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'

"""
def string_splosion(str):
    result = ""
    for x in range(len(str)):
        result += str[:x + 1]
    return result
########################################################################################################
"""


Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the 
last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

"""

def last2(str):
    # Screen out too-short string case.
    if len(str) < 2:
        return 0

    # last 2 chars, can be written as str[-2:]
    last2 = str[len(str) - 2:]
    count = 0

    # Check each substring length 2 starting at i
    for i in range(len(str) - 2):
        sub = str[i:i + 2]
        if sub == last2:
            count = count + 1

    return count
############################################################################################################


def binary_search(lst, key):
    low = 0
    high = len(lst) - 1
    while high >= low:
        mid = low + (high - low) // 2
        if key < lst[mid]:
            high = mid - 1
            print("Bob")
        elif key > lst[mid]:
            low = mid + 1
            print("Jim")
        else:
            print("Kendall")
            return mid
    return -low - 1


print(binary_search(['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'C'))


#Testers Reviewers

# Look over lists and stuff -> deep copy, direct copies, M = list[L]

# Subclass and superclass
# Is - A relationship -> a human is a mammal, an apple is a fruit
# Has - A relationship -> properties specific to an object - a student has an id number
# Abstract class -> have abstract properties or methods - typically cannot be instantiated
# Encapsulation -> everything that you need to model a class has been enclosed to make it nice and clean
# Constructor chaining->
# Operator overloading->
# Overriding -> reproduce the same method with the subclass and give it more specific methods - Employee manager

# Search methods to know: sequential search, binary search, selection sort

# Type vs isinstance -> isinstance considers all the ways up- is human an instance of a mammal and an object? Yee.
# Is the type of human a mammal? No, the type of human is a human.

# Overwritten is bs, overridden

# Public and private variables