#
# life.py - Game of Life lab
#
# Name: Jerry Cheng
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#

import random
import sys


def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row


def createBoard(width, height):
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A


# A = createBoard(5, 3)
# print(A)

def printBoard(A):
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')


# A = createBoard(5, 3)
# printBoard(A)

def diagonalize(width, height):
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A


# A = diagonalize(7, 6)
# print(A)

def innerCells(width, height):
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if (row != 0 and row != height - 1) and (col != 0 and col != width - 1):
                A[row][col] = 1
    return A


# A = innerCells(5, 5)
# printBoard(A)

def randomCells(width, height):
    A = innerCells(width, height)
    for row in range(height):
        for col in range(width):
            if A[row][col] == 1:
                A[row][col] = random.choice([0, 1])
    return A


# A = randomCells(10, 10)
# printBoard(A)

def copy(A):
    copy = []
    for row in range(len(A)):
        newRow = []
        for column in range(len(A[row])):
            newRow.append(A[row][column])
        copy.append(newRow)
    return copy


def innerReverse(A):
    result = copy(A)
    height = len(result)
    width = len(result[0])
    for row in range(height):
        for column in range(width):
            if (row == 0 or row == height - 1) or (column == 0 or column == width - 1):
                result[row][column] = 0
            elif result[row][column] == 1:
                result[row][column] = 0
            else:
                result[row][column] = 1
    return result


def next_life_generation(A):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            sum = 0
            if i == 0 or i == len(A) - 1 or j == 0 or j == len(A[i]) - 1:
                row.append(0 * j)
                continue
            for neighbor_i in range(i - 1, i + 2):
                for neighbor_j in range(j - 1, j + 2):
                    sum += A[neighbor_i][neighbor_j]
            if A[i][j] == 1:
                row.append(1 if sum - A[i][j] == 3 or sum - A[i][j] == 2 else 0)
            else:
                row.append(1 if sum - A[i][j] == 3 else 0)
        result.append(row)
    return result
