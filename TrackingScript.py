from Helpers.HelperScripts import Position
from Helpers.ParsingScript import parse_trades
from PricingRequests import current_price

# Runs prior to anything else; runs main at end
def startup():
    # PRE MAIN

    # MAIN
    main()

    # POST MAIN
    

# Takes the trades in from the csv and puts them into positions.
# Returns dictionary of open positions with ticker : quantity (key : pair)
def parse_positions():
    ticker_cache = []
    positions = []
    for trade in parse_trades():
        # Open positions for each new trade
        # Otherwise, log an update in quantity to the positions object which already exists
        if not (trade.ticker in ticker_cache):
            ticker_cache.append(trade.ticker)
            new_pos = Position(trade)
            positions.append(new_pos)

        else:
            for position in positions:
                if position.ticker == trade.ticker:
                    position.new_trade(trade)
                    break

    return positions

def open_positions(positions):
    open = []
    for position in positions:
        if position.open:
            open.append(position)

    return open

def display_positions(positions):
    print("Ticker\t\tQuantity\t\tPrice\t\tValue")

    for pos in sorted(positions, key=lambda x: x.current_value, reverse=True):
        print(pos)

# Main function to track and record trades
def main():
    positions = parse_positions()
    positions = current_price(positions)
    display_positions(positions)


if __name__ == "__main__":
    startup()
    
