'''
Created on 30 October 2018

jcheng15

I pledge my honor that I have abided by the Stevens Honor System.
'''

def TcToNum(x):
    """ Takes as input a string, x, of 8 bits representing an integer in two's complement, and returns the
    corresponding integer"""
    def TcToNumHelper(x):
        if x == "":
            return 0
        return TcToNumHelper(x[:-1]) * 2 + int(x[-1])
    return TcToNumHelper(x[1:]) if x[0] == "0" else TcToNumHelper(x[1:]) - 128

def NumToTC(N):
    """Takes as input integer N and returns a string representing the two's complement representation
    of that integer"""
    def numToBinary(n):
        """ Converts a number to binary """
        if n == 0:
            return ""
        return numToBinary(int(n / 2)) + str(n % 2)

    def fillDigits(s):
        """ If N is not already in 8 bits, adds enough 0's to do so"""
        return "0" * (7 - len(s)) + s

    if N < -128 or N >= 128:
        return "Error"
    if N >= 0:
        return "0" + fillDigits(numToBinary(N))
    else:
        return "1" + fillDigits(numToBinary(N + 128))