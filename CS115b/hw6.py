'''
Created on 15 October 2018
@author:   jcheng15
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

Partner: Reilly Fitzgerald

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''

    if n == 0:
        return ""
    return numToBinary(n // 2) + str(n % 2)

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''

    if s == "":
        return 0
    return binaryToNum(s[:-1]) * 2 + int(s[-1:])

def numToBinaryPadded(n):
    '''Pads the Binary number.'''
    s = numToBinary(n)
    return "0" * (COMPRESSED_BLOCK_SIZE - len(s)) + s

def prefixLen(s):
    '''Finds the length of number of occurrences of the prefix.'''
    if len(s) == 1:
        return 1
    if s[1] == s[0]:
        return 1 + prefixLen(s[1:])
    return 1

def compress(s):
    '''Takes a binary string(S) of length 64 as input and returns another binary string as output.
    The output binary string should be a run-length encoding of the index string.'''
    def compressHelp(s, b):
        if s == "":
            return ""
        if s[0] != chr(b + ord("0")):
            return numToBinaryPadded(0) + compressHelp(s, 1 - b)
        prefix_len = min(prefixLen(s), MAX_RUN_LENGTH)
        return numToBinaryPadded(prefix_len) + compressHelp(s[prefix_len:], 1 - b)
    return compressHelp(s, 0)

# 325 Because 64*5 is 320. You can have 5 leading zeroes if the original string begins with a 1.

def uncompress(s):
    """Inverts or undoes the compressing in the compress function."""
    def uncompressHelp(s, b):
        if s == "":
            return ""
        n = binaryToNum(s[:COMPRESSED_BLOCK_SIZE])
        return chr(b + ord("0")) * n + uncompressHelp(s[COMPRESSED_BLOCK_SIZE:], 1 - b)
    return uncompressHelp(s, 0)

def compression(s):
    """Returns the ratio of the compressed size to the original size for image S."""
    return len(compress(s)) / len(s)

# Penguin
# print(compression("00011000" + "00111100" * 3 + "01111110" + "11111111" + "00111100"+ "00100100"))
# Smile
# print(compression("0" * 8 + "01100110" * 2 + "0" * 8 + "00001000" + "01000010" + "01111110" + "0" * 8))
# Five
# print(compression("1" * 9 + "0" * 7 + "10000000" * 2 + "1" * 7 + "0" + "00000001" * 2 + "1" * 7 + "0"))
#
# Penguin: 1.484
# Smile: Ratio of 1.328
# Five: 1.015

"""The reason that Professor Lai is false because using binary, one cannot always simplify multiple bits into less bits
as each bit has only 2 possible values, where each group of bits has 2^n values"""