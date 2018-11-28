'''
Created on 26 November 2018
@author:   jcheng15
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

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
        '''Returns a new object with the same month, day, year as the calling object (self). '''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date, whether or not they are in
        the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and self.day == d2.day

    def tomorrow(self):
        '''This method does not return anything, but instead changes the calling object so that 
        it represents one calendar day after the date it originally appeared.'''
        days_in_month = DAYS_IN_MONTH[self.month]
        if days_in_month == 28 and self.isLeapYear() is True:
            days_in_month = 29
        if self.day + 1 <= days_in_month:
            self.day += 1
        else:
            self.day = 1
            self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1

#d = Date(2,28,2016)
#d.tomorrow()
#print(d)

    def yesterday(self):
        '''Like tomorrow, this method should not return anything, but instead should change the calling object
        so that it represents one calendar day before it originally represented'''
        days_in_month = DAYS_IN_MONTH[self.month - 1]
        if days_in_month == 28 and self.isLeapYear() is True:
            days_in_month = 29
        if days_in_month == 0:
            days_in_month = DAYS_IN_MONTH[12]
        if self.day - 1 > 0:
            self.day -= 1
        else:
            self.day = days_in_month
            self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1

#d = Date(3,1,2016)
#d.yesterday()
#print(d)

    def addNDays(self, N):
        '''Changes the calling object so that it represents N calendar days after the date it originally
        represented'''
        for x in range(N):
            print(self)
            self.tomorrow()
        print(self)

# d = Date(11, 9, 2011)
# d.addNDays(3)
# print(d)

    def subNDays(self, N):
        '''Changes the calling object so that it represents N calendar days before the date it originally
        represented'''
        for x in range(N):
            print(self)
            self.yesterday()
        print(self)

#d = Date(1, 1, 2017)
#d.subNDays(366)
#print(d)

    def isBefore(self, d2):
        '''This method should return True if the calling object is a calendar date before the input
        named d2, and returns False otherwise'''
        if self.year > d2.year:
            return False
        if self.year == d2.year and self.month > d2.month:
            return False
        if self.year == d2.year and self.month == d2.month and self.day > d2.day:
            return False
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return False
        return True

#d = Date(3, 1, 2012)
#d2 = Date(1, 1, 2012)
#print(d.isBefore(d2))

    def isAfter(self, d2):
        '''This method should return True if the calling object is a calendar date after the input
        named d2, and returns False otherwise'''
        if self.year < d2.year:
            return False
        if self.year == d2.year and self.month < d2.month:
            return False
        if self.year == d2.year and self.month == d2.month and self.day < d2.day:
            return False
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return False
        return True

#d = Date(1, 1, 2011)
#d2 = Date(1, 1, 2012)
#print(d.isAfter(d2))

    def diff(self, d2):
        '''This method should return an integer representing the number of days between self and d2.
        Think of it representing self - d2'''
        count = 0
        self_copy = self.copy()
        d2_copy = d2.copy()
        if (d2_copy).equals(self_copy):
            return count
        while self_copy.isBefore(d2_copy):
            self_copy.tomorrow()
            count -= 1
        while self_copy.isAfter(d2_copy):
            self_copy.yesterday()
            count += 1
        return count

#d = Date(11, 9, 2011)
#d2 = Date(12, 16, 2011)
#print(d2.diff(d))

    def dow(self):
        '''This method returns a string that indicates the day of the week of the object that calls it.'''
        days = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
        given_date = Date(11, 9, 2011)
        day_diff = self.diff(given_date)
        day = day_diff % 7
        return days[day]

d = Date(10, 28, 1929)
print(d.dow())