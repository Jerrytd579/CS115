'''
Created on 11/24/2018
@author:   Corinne Wisniewski
Pledge:   "I pledge my honor that I have abided by the Stevens Honor System." -cwisnie1

CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''         
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and self.day == d2.day 
    
    def tomorrow(self):
        """method will not return anything, but changes the
        calling object so that it represents one calendar 
        day after the date it originally represented"""
        if self.day < DAYS_IN_MONTH[self.month]:
            self.day += 1
        else:
            if self.isLeapYear() and self.month == 2 and self.day < 29:
                self.day += 1
            self.day = 1
            if self.month < 12:
                self.month += 1
            else:
                self.month = 1
                self.year += 1

    def yesterday(self):
        """method will not return anything, but changes the
        calling object so that it represents one calendar
        day before the date it originally represented"""
        if self.day - 1 > 0:
            self.day -= 1
        else:
            if self.month == 3:
                if self.isLeapYear():
                    self.day = 29
                    self.month = 2
                    return
            if self.month == 1:
                self.month = 12
                self.day = 31
                self.year -= 1
            else:
                self.day = DAYS_IN_MONTH[self.month - 1]
                self.month -= 1

    def addNDays(self, N):
        """assume N is non negative. will not return anything, but
        should change the calling object so that it represents N
        calendar days after the date it originally represented"""
        if N >= 0:
            for _ in range(N):
                print(self)
                self.tomorrow()
        print(self)

    def subNDays(self, N):
        """assume N is non negative. will not return anything, but
        should change the calling object so that it represents N
        calendar days before the date it originally represented"""
        if N >= 0:
            for _ in range(N):
                print(self)
                self.yesterday()
        print(self)

    def isBefore(self, d2):
        if d2.year == self.year:
            if d2.month == self.month:
                if self.day < d2.day:
                    return True
                else:
                    return False
            elif self.month < d2.month:
                return True
            else:
                return False
        elif self.year < d2.year:
            return True
        else:
            return False

    def isAfter(self, d2):
        """method should return true if the calling object is
        a calendar date after the input d2. should return false
        if date is the same or if date is before d2"""
        if self.equals(d2):
            return False
        return not self.isBefore(d2)

    def diff(self, d2):
        """returns an integer representing the number of days
        between self and d2"""
        #use tomorrow and yesterday methods and a while loop
        if self.equals(d2):
            return 0
        comparison = Date(self.month, self.day, self.year)
        if self.isBefore(d2):
            increment = 1
        else:
            increment = -1
        number_of_days = 0
        while True:
            number_of_days += increment
            if increment == 1:
                comparison.tomorrow()
            else:
                comparison.yesterday()
            if comparison.equals(d2):
                return - number_of_days

    def dow(self):
        """returns a string indicating the day of the week of
        the object that calls it. could be monday, tuesday, etc"""
        lst = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
        return lst[self.diff(Date(11, 21, 2018)) % 7]
