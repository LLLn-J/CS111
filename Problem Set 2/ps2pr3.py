# Hu Xuan 7/7/2022
# xuanh@bu.edu
# Problem Set 2, Problem 3
# ps2pr3.py
# Validating Data

def is_valid_month(month):
    """ The function returns True if the month is valid,
    and False otherwise.
    """
    return 0 < month < 13


def is_leap_year(year):
    """ The function returns True if the year is
    a leap year, and False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        else:
            return True
    else:
        return False


def is_valid_day_in_month(month, day, year):
    """ The function returns True if the day number
    is valid within the month, and False otherwise.
    """
    if is_valid_month(month):
        if (month == 1 or month == 3 or month == 5 or  # for bigger months
                month == 7 or month == 8 or month == 10 or month == 12):
            if 1 <= day <= 31:
                return True
        elif month == 4 or month == 6 or month == 9 or month == 11:  # for regular smaller months
            if 1 <= day <= 30:
                return True
        else:
            if is_leap_year(year):
                if 1 <= day <= 29:
                    return True
            else:
                if 1 <= day <= 28:
                    return True
    return False


def get_month_name(month):
    """ This function takes an integer parameter month
    and must return the name of the month as a string.
    """
    names = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
             "November", "December"]
    return names[month]


def is_valid_date(month, day, year):
    """ takes integer parameters for the month, day, and year,
    and then returns True if this is a valid date and False
    if it is not a valid date.
    """
    str_month = str(month)
    str_day = str(day)
    str_year = str(year)
    if is_valid_month(month):
        if is_valid_day_in_month(month, day, year):
            print(str_month + "/" + str_day + "/" + str_year + " is a valid date")
            return True
        else:
            print(
                str_month + "/" + str_day + "/" + str_year + " is a not valid date, because day " + str_day +
                " is not valid date for " + get_month_name(month) + " " + str_year)
            return False

    else:
        print(str_month + "/" + str_day + "/" + str_year + " is a not valid date, because " +
              str_month + " is not valid month")
        return False


if __name__ == '__main__':
    # test for is_leap_year
    print(is_leap_year(2012))
    print(is_leap_year(1900))
    print(is_leap_year(2013))
    print(is_leap_year(2000))

    # test for is_valid_day_in_month
    print(is_valid_day_in_month(8, 31, 2012))
    print(is_valid_day_in_month(7, 31, 2012))
    print(is_valid_day_in_month(2, 31, 2012))
    print(is_valid_day_in_month(3, 31, 2012))
    print(is_valid_day_in_month(2, 29, 2012))
    print(is_valid_day_in_month(2, 29, 1959))

    # test for get_month_name
    print(get_month_name(9))

    # test for is_valid_date
    print(is_valid_date(2, 29, 2016))
    print(is_valid_date(2, 29, 2017))
    print(is_valid_date(2, 29, 2018))
    print(is_valid_date(1, 32, 2018))
    print(is_valid_date(13, 7, 2018))
