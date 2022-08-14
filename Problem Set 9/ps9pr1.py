# Hu Xuan 8/3/2022
# xuanh@bu.edu
# Problem Set 9, Problem 1
# ps9pr1.py
# A Date class

class Date:
    """ A class that stores and manipulates dates,
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, new_month, new_day, new_year):
        """ The constructor for objects of type Date. """
        self.month = new_month
        self.day = new_day
        self.year = new_year

    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

    #### Put your code below. ####

    def advance_one(self):
        """ changes the called object so that it represents one calendar
        day after the date that it originally represented.
        """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year():
            days_in_month[2] = 29
        self.day += 1
        if self.day > days_in_month[self.month]:
            self.day = 1
            self.month += 1
        if self.month > 12:
            self.year += 1
            self.month = 1

    def advance_n(self, n):
        """ changes the calling object so that it represents n calendar
        days after the date it originally represented.
        """
        print(self)
        for i in range(n):
            self.advance_one()
            print(self)

    def __eq__(self, other):
        """ returns True if the called object (self) and the argument
        (other) represent the same calendar date (i.e., if they have the
        same values for their day, month, and year attributes).
        """
        if self.day != other.day or self.month != other.month or self.year != other.year:
            return False
        return True

    def is_before(self, other):
        """ returns True if the called object represents a calendar date
        that occurs before the calendar date that is represented by others.
        """
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False
        else:
            if self.month < other.month:
                return True
            elif self.month > other.month:
                return False
            else:
                if self.day < other.day:
                    return True
                else:
                    return False

    def is_after(self, other):
        """ returns True if the calling object represents a calendar date
        that occurs after the calendar date that is represented by others.
        If self and other represent the same day, or if self occurs before
        other, the method should return False.
        """
        if not self.is_before(other):
            if self != other:
                return True
        return False

    def days_between(self, other):
        """ returns an integer that represents the number of days between self and other.
        """
        before = other.copy()
        after = self.copy()
        if self.is_before(other):
            before = self.copy()
            after = other.copy()
        count = 0
        while before != after:
            before.advance_one()
            count += 1
        if self.is_before(other):
            count = 0 - count
        return count

    def day_name(self):
        """ returns a string that indicates the name of the day of
        the week of the Date object that calls it.
        """
        day_names = ['Monday', 'Tuesday', 'Wednesday',
                     'Thursday', 'Friday', 'Saturday', 'Sunday']
        base = Date(6, 14, 2021)
        between = self.days_between(base)
        name = day_names[0 + between % 7]
        return name
