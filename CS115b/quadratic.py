'''
Jerry Cheng

I pledge my honor that I have abided by the Stevens Honor System.

'''

import math

class QuadraticEquation(object):
    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        else:
            self.__a = float(a)
            self.__b = float(b)
            self.__c = float(c)

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def c(self):
        return self.__c

    def discriminant(self):
        return self.__b ** 2 - 4 * self.__a * self.__c

    def root1(self):
        discriminant = self.discriminant()
        if discriminant < 0:
            return None
        return (-1 * self.__b + math.sqrt(discriminant)) / (2 * self.__a)

    def root2(self):
        discriminant = self.discriminant()
        if discriminant < 0:
            return None
        return (-1 * self.__b - math.sqrt(discriminant)) / (2 * self.__a)

    def __str__(self):
        if self.__a < 0:
            a_sign = '-'
        else:
            a_sign = ''
        if self.__b < 0 or self.__c < 0:
            b_sign = '-'
        else:
            b_sign = '+'
        if self.__c < 0:
            c_sign = '-'
        else:
            c_sign = '+'
        if self.__a == 1 or self.__a == -1:
            a = ''
        else:
            a = str(abs(self.__a))
        if self.__b == 0:
            b = ''
        elif self.__b == 1 or self.__b == -1:
            b = b_sign + ' x '
        else:
            b = b_sign + ' ' + str(abs(self.__b)) + 'x '
        if self.__c == 0:
            c = ''
        else:
            c = c_sign + ' ' + str(abs(self.__c)) + ' '
        return a_sign + a + 'x^2 ' + b + c + '= 0'

print(QuadraticEquation(2, 4, 6))