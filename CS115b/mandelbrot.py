# mandelbrot.py
# Lab 9
#
# Name: Jerry Cheng
# I pledge my honor that I have abided by the Stevens Honor System.

# keep this import line...
from cs5png import PNGImage


# start your Lab 9 functions here:

def mult(c, n):
    ''' Returns the product of c times n without multiplication '''
    result = 0
    for x in range(n):
        result += c
    return result


def update(c, n):
    ''' Starts a new value, z, at zero, and then repeatedly updates the value of z using the assignment
    statement z = z**2 + c for a total of n times '''
    result = 0
    for x in range(n):
        if x == n:
            return result
        result = result ** 2 + c
    return result


def inMSet(c, n):
    ''' inMSet takes in c for the update step of z = z** 2 + c n, the maximum number of times to run that step.
    Then, it should return False as soon as abs(z) gets larger than 2. True if abs(z) never
    gets larger than 2 (for n iterations).'''
    z = 0
    for x in range(n):
        z = z ** 2 + c
        if abs(z) > 2:
            return False
    return True


def weWantThisPixel(col, row):
    if col % 10 == 0 and row % 10 == 0:
        return True
    else:
        return False


def test():
    ''' A function to demonstrate how to create and save a png image'''
    width = 300
    height = 200
    image = PNGImage(width, height)

    for col in range(width):
        for row in range(height):
            if weWantThisPixel(col, row) == True:
                image.plotPoint(col, row)

    image.saveFile()


# If we were to change line 41, if col % 10 == 0 and row % 10 == 0 and replaced the and statement with an or, we would
# end up with a grid of lines rather than dots

test()


def scale(pix, pixelMax, floatMin, floatMax):
    ''' Scale takes in:
        pix, the CURRENT pixel column (or row)
        pixMax, the total # of pixel columns
        floatMin, the minimum floating point value
        floatMax, the maximum floating point value
        scale returns floating-point value that corresponds to pix
    '''
    return ((pix / pixelMax) * (floatMax - floatMin)) + floatMin


# print(scale(100, 200, -2.0, 1.0))
# print(scale(100, 200, -1.5, -1,5))

def mset():
    ''' Creates a 300x200 image of the Mandelbrot set'''
    width = 300
    height = 200

    image = PNGImage(width, height)

    for col in range(width):
        for row in range(height):
            x = scale(col, width, -2, 1)
            y = scale(row, height, -1, 1)
            c = x + y * 1j
            if inMSet(c, 25) == True:
                image.plotPoint(col, row)
    image.saveFile()


mset()
