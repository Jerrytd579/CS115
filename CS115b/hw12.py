'''

Jerry Cheng

jcheng15

I pledge my honor that I have abided by the Stevens Honor System.

5 October 2018

'''


class Board(object):
    def __init__(self, width=7, height=6):
        '''A constructor for Board objects that takes two named arguments, one for the number of rows
        and one for the number of columns. Creates a board variable containing the current board layout.'''
        self.__width = width
        self.__height = height
        board = []
        for i in range(height):
            row = []
            for i in range(width):
                row.append(' ')
            board.append(row)
        self.__board = board

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def __str__(self):
        '''Prints out the board layout'''
        result = ''
        for i in range(len(self.__board)):
            result += '|'
            for s in self.__board[i]:
                result += s + '|'
            result += '\n'
        for i in range(len(self.__board[0]) * 2 + 1):
            result += '-'
        result += '\n'
        for i in range(len(self.__board[0])):
            result = result + ' ' + str(i)
        return result

    def allowsMove(self, col):
        '''Returns True if the calling Board object can allow a move into column c. Returns false
        if c does not have space available or if it is not a valid column'''
        if col < self.__width and col >= 0:
            for row in range(self.__width - 1):
                if self.__board[row][col] == ' ':
                    return True
        return False

    def addMove(self, col, ox):
        '''Adds an ox checker, where ox is a variable holding a string that is either X or O into column
        col'''
        if self.allowsMove(col) == True:
            if self.__board[self.__height - 1][col] == ' ':
                self.__board[self.__height - 1][col] = ox
            else:
                for row in range(self.__width - 2):
                    if self.__board[row][col] == ' ' and \
                            self.__board[row + 1][col] != ' ':
                        self.__board[row][col] = ox

    def setBoard(self, moveString):
        """ takes in a string of columns and places
        alternating checkers in those columns,
        starting with 'X'

        For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to
        see them alternate in the left column.
        moveString must be a string of integers
        """

        nextCh = 'X'  # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh = 'X'

    def delMove(self, col):
        """Does the opposite of add move - should remove the top checker from the column col"""
        for row in range(self.__width - 2):
            if self.__board[row][col] == ' ' and self.__board[row + 1][col] != ' ':
                self.__board[row + 1][col] = ' '
                break

    def winsFor(self, ox):
        """ Returns true or false if X or O has won, checking the calling board"""

        # Horizontally
        for row in range(self.__height):
            for col in range(self.__width - 3):
                if self.__board[row][col] == ox and \
                        self.__board[row][col + 1] == ox and \
                        self.__board[row][col + 2] == ox and \
                        self.__board[row][col + 3] == ox:
                    return True

        # Vertically
        for row in range(self.__height - 3):
            for col in range(self.__width):
                if self.__board[row][col] == ox and \
                        self.__board[row + 1][col] == ox and \
                        self.__board[row + 2][col] == ox and \
                        self.__board[row + 3][col] == ox:
                    return True

        # Top left to bottom right
        for col in range(self.__width - 3):
            for row in range(self.__height - 3):
                if self.__board[row][col] == ox and \
                        self.__board[row + 1][col + 1] == ox and \
                        self.__board[row + 2][col + 2] == ox and \
                        self.__board[row + 3][col + 3] == ox:
                    return True

        # Bottom left to top right
        for row in range(self.__height):
            for col in range(self.__width - 3):
                if self.__board[row][col] == ox and \
                        self.__board[row - 1][col + 1] == ox and \
                        self.__board[row - 2][col + 2] == ox and \
                        self.__board[row - 3][col + 3] == ox:
                    return True

        return False

    def hostGame(self):
        """ Creates a user interface to run the game"""
        print("Welcome to Connect4!")
        player = "X"
        choice = -1
        print(self)
        print()
        while True:
            correctInput = 0
            while correctInput == 0:
                if player == "X":
                    try:
                        choice = int(input("Player X's choice: "))
                        correctInput = 1
                    except ValueError:
                        correctInput = 0
                else:
                    try:
                        choice = int(input("Player O's choice: "))
                        correctInput = 1
                    except ValueError:
                        correctInput = 0
                if correctInput == 1 and self.allowsMove(choice):
                    correctInput = 1
                else:
                    print("Invalid value! Please input a valid integer column section between 0 and " + str(
                        self.__width - 1))
                    correctInput = 0
            if player == "X":
                self.addMove(choice, "X")
                player = "O"
            else:
                self.addMove(choice, "O")
                player = "X"
            print()
            if self.winsFor("X"):
                print()
                print("Congratulations! Player X wins!")
                print()
                print(self)
                exit()
            if self.winsFor("O"):
                print()
                print("Congratulations! Player O wins!")
                print()
                print(self)
                exit()
            print(self)
            print()


if __name__ == '__main__':
    '''if this is the main function, run the hostgame on a standard board'''
    b = Board()
    b.hostGame()
