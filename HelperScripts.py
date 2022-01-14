import csv
import datetime

# Records either the start or end date of a position
def record_date(trade, direction):
    if direction == "START":
        with open("Dates.csv", "a") as dates_csv:
            dates_csv.write("{},{},{},{},,,\n".format(trade.ticker, trade.day, trade.month, trade.year))
    elif direction == "END":
        trades = []
        to_change = []
        with open("Dates.csv", "r") as dates_csv:
            for row in dates_csv:
                row = row.split(",")
                if row[0] == trade.ticker:
                    row[4] = trade.day
                    row[5] = trade.month
                    row[6] = trade.year
                    to_change = row
                else:
                    trades.append(row)
        with open("Dates.csv", "w") as dates_csv:
            dates_csv.write("{},{},{},{},{},{},{}\n".format(to_change[0], to_change[1], to_change[2], to_change[3],
                                                            to_change[4], to_change[5], to_change[6]))
            for trade in trades:
                if len(trade) != 7:
                    continue
                dates_csv.write("{},{},{},{},{},{},{}".format(trade[0], trade[1], trade[2],
                                                                trade[3], trade[4], trade[5], trade[6]))
                
    else:
        return None

# Open position dates are set to today
def clean_dates():
    trades = []
    with open("Dates.csv", "r") as dates_csv:
        for trade in dates_csv:
            if trade.split(",")[5] == "":
                trade = trade.split(",")
                trade[4] = datetime.datetime.now().day
                trade[5] = datetime.datetime.now().month
                trade[6] = datetime.datetime.now().year
                trade = "{},{},{},{},{},{},{}\n".format(trade[0], trade[1], trade[2], trade[3], trade[4], trade[5], trade[6])
                trades.append(trade)
            else:
                (trades.append(trade))
    with open("Dates.csv", "w") as dates_csv:
        for trade in trades:
            dates_csv.write(trade)