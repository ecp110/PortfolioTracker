import csv
import datetime

# Hold each trade information
class Trade:
    day = -1
    month = -1
    year = -1
    ticker = None
    exchange = None
    quantity = -1
    price = -1
    comission = -1

    def __init__(self, day, month, year, ticker, exchange, quantity, price, comission):
        self.day = day
        self.month = month
        self.year = year
        self.ticker = ticker
        self.exchange = exchange
        self.quantity = quantity
        self.price = price
        self.comission = comission

    def __str__(self):
        return "{} of {} on {}/{}/{} for ${}/sh.".format(self.quantity, self.ticker, self.day, self.month, self.year, self.price)

# Parses trades from csv into Trade objects
# Returns list of trade objects
def parse_trades():
    trades = []
    with open("Data/PortfolioInfo.csv", "r") as portfolio_csv:
        portfolio_raw = csv.reader(portfolio_csv, delimiter = ",")
        x = 0
        for raw_trade in portfolio_raw:
            if x == 0:
                x = 1
                continue
        
            try:
                day = int(raw_trade[0])
                month = int(raw_trade[1])
                year = int(raw_trade[2])
                ticker = raw_trade[3]
                exchange = raw_trade[4]
                price = float(raw_trade[6])
                comission = float(raw_trade[8])

                # Sells have a negative quantity
                if raw_trade[7] == "BUY":
                    quantity = float(raw_trade[5])
                else:
                    quantity = float(raw_trade[5]) * -1
            except Exception as e:
                print(e)
                return None
            
            trades.append(Trade(day, month, year, ticker, exchange, quantity, price, comission))
    return trades