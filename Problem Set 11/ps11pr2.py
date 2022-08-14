# Hu Xuan 8/10/2022
# xuanh@bu.edu
# Problem Set 11, Problem 2
# ps11pr2.py
# Holiday clients

from ps11pr1 import Holiday
from ps9pr1 import Date


def get_holidays(year):
    """ returns a list of the Holidays for any given year.
    """
    holidays = []

    nyd = Holiday(1, 1, year, "New Year’s Day")
    if nyd.day_name() == 'Sunday':
        nyd.day = 2
    holidays += [nyd]

    mlkd = Holiday(1, 1, year, "Martin Luther King Day")
    count = 0
    while mlkd.day_name() != "Monday" or count < 3:
        if mlkd.day_name() == "Monday":
            count += 1
        if count == 3:
            break
        mlkd.advance_one()
    holidays += [mlkd]

    pd = Holiday(2, 1, year, "President’s Day")
    count = 0
    while pd.day_name() != "Monday" or count < 3:
        if pd.day_name() == "Monday":
            count += 1
        if count == 3:
            break
        pd.advance_one()
    holidays += [pd]

    md = Holiday(5, 31, year, "Memorial Day")
    while md.day_name() != "Monday":
        md.day -= 1
    holidays += [md]

    juneteenth = Holiday(6, 19, year, "Juneteenth")
    if juneteenth.day_name() == 'Sunday':
        nyd.day = 20
    holidays += [juneteenth]

    ind = Holiday(7, 4, year, "Independence Day")
    if ind.day_name() == 'Sunday':
        ind.day = 5
    holidays += [ind]

    ld = Holiday(9, 1, year, "Labor Day")
    while ld.day_name() != "Monday":
        ld.advance_one()
    holidays += [ld]

    ipd = Holiday(10, 1, year, "Indigenous People’s Day")
    count = 0
    while ipd.day_name() != "Monday" or count < 2:
        if ipd.day_name() == "Monday":
            count += 1
        if count == 2:
            break
        ipd.advance_one()
    holidays += [ipd]

    td = Holiday(11, 1, year, "Thanksgiving Day")
    count = 0
    while td.day_name() != "Thursday" or count < 4:
        if td.day_name() == "Thursday":
            count += 1
        if count == 4:
            break
        td.advance_one()
    holidays += [td]

    cd = Holiday(12, 25, year, "Christmas Day")
    if cd.day_name() == "Sunday":
        cd.day = 26
    holidays += [cd]

    return holidays


def closest_holiday(date):
    """ find the Holiday that is closest to that parameter date, which is a Date object.
    """
    this_holidays = get_holidays(date.year)
    next_holidays = get_holidays(date.year + 1)
    last_holidays = get_holidays(date.year - 1)
    count_lst_this = [(abs(date.days_between(h)), h) for h in this_holidays]
    count_lst_next = [(abs(date.days_between(h)), h) for h in next_holidays]
    count_lst_last = [(abs(date.days_between(h)), h) for h in last_holidays]
    comp = [min(count_lst_this), min(count_lst_next), min(count_lst_last)]
    return min(comp)[1]


date = Date(12, 29, 2020)
h = closest_holiday(date)
print(h, 'is the closest holiday to', date)
# if __name__ == '__main__':
#
#     ## TEST CODE:
#     holidays = get_holidays(2023)
#     print()  # blank line
#     for h in holidays:
#         print(h, "is observed on a", h.day_name())
