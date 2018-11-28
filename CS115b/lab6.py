'''
Created on 10 October 2018
@author:   jcheng15
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''


def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 0:
        return False
    return True

# 42 in base 2 is 00101010

# The least significant part of an odd number will be 1, and the least significant part of an even will be 0.
# This is because the last digit of the number represents 2^0, determining whether or not the number is odd or even.
# Every other digit in the binary number ends up even.

# The original number ends up being divided by 2. If the number is odd, the result rounds down.

# If N is even, we would return the value with a 0 at the end.
# If N is odd, we would return the value with a 1 at the end.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''

    if n == 0:
        return ""
    return numToBinary(int(n / 2)) + str(n % 2)

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''

    if s == "":
        return 0
    return binaryToNum(s[:-1]) * 2 + int(s[-1:])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''

    return ("0" * 8 + numToBinary(binaryToNum(s) + 1))[-8:]

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == 0:
        print(s)
        return s
    print(s)
    return count(increment(s), n - 1)

# The ternary value for 59 ends up being 2012. THis is because:
# 59/3 = 19 R2, 19/3= 6 R 1,6/3 = 2 R 0, and 2/3 = 0 R 2.
# You then combine the remainders from right to left, thus being 2012.

def numToTernary(n):
    '''Precondition: integer argument is non-negtive.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    return numToTernary(int(n / 3)) + str(n % 3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    return ternaryToNum(s[:-1]) * 3 + int(s[-1])
