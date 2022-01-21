# Position class to hold info on a position
class Position:
    def __init__(self, trade):
        # Status values
        self.ticker = trade.ticker
        self.open = True
        self.exchange = trade.exchange

        # Pricing / numerical values
        self.quantity = 0
        self.current_price = 0
        self.current_value = 0
        self.time_quantity = {}

        # Establishes first trade to open position
        self.new_trade(trade)
    
    def __str__(self):
        return "{}\t\t{}\t\t${}\t\t${}".format(self.ticker, self.quantity, self.current_price, self.current_value)

    def new_trade(self, trade):
        date = "{}/{}/{}".format(trade.day, trade.month, trade.year)
        self.time_quantity[date] = self.quantity + trade.quantity
        self.quantity += trade.quantity

        if self.quantity == float(0):
            self.open = False
        else:
            self.open = True
    
    def set_price(self, price):
        self.current_price = price
        self.current_value = self.current_price * self.quantity

# Converts normal date to Yahoo time (UNIX epoch seconds)
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