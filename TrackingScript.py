from ParsingScript import parse_trades
from HelperScripts import record_date
from HelperScripts import clean_dates

# Runs prior to anything else; runs main at end
def startup():
    with open("Dates.csv", "w") as dates_csv:
        dates_csv.write("")
    
    main()
    clean_dates()

# Main function to track and record trades
def main():
    ticker_cache = {}
    for trade in parse_trades():
        if trade.ticker in ticker_cache.keys():
            if trade.direction == "BUY":
                ticker_cache[trade.ticker] = ticker_cache[trade.ticker] + trade.quantity
            elif trade.direction == "SELL":
                ticker_cache[trade.ticker] = ticker_cache[trade.ticker] - trade.quantity
            else:
                raise Exception("Direction of trade is incorrect for trade {}".format(trade))
        else:
            ticker_cache[trade.ticker] = trade.quantity
            record_date(trade, "START")

        x = 0
        while x < len(ticker_cache.keys()):
            ticker = list(ticker_cache.keys())[x]
            if ticker_cache[ticker] == 0:
                record_date(trade, "END")
                ticker_cache.pop(ticker)
            x += 1

    for trade in ticker_cache:
        print("{} {}".format(trade, ticker_cache[trade]))
        
if __name__ == "__main__":
    startup()
    
