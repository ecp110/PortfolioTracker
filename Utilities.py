def date_to_yh(day, month, year):
    month_days = {
        1 : 31,
        2 : 28,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31,
    }

    DAY_TO_YAHOO = 60*60*24
    YAHOO_TO_DAY = 1/(60*60*24)
    # Check that, if current year is leap year, it is adjusted (1 more day)
    if year%4 == 0 or (year%100 == 0 and year%400 == 0):
        yh_days = 1
    else:
        yh_days = 0

    # Figure out how many full leap years have passed
    leap_years = 0
    x = 1970
    while x < year:
        if x%4 == 0 or (x%100 == 0 and x%400 == 0):
            leap_years += 1
        x += 1

    year = (year - 1970) - leap_years
    day -= 1

    yh_days += day
    yh_days += leap_years * 366
    yh_days += year * 365
    while month > 1:
        yh_days += month_days[month]
        month -= 1

    yh_days = yh_days * DAY_TO_YAHOO

    return yh_days