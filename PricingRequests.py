import requests
import time
from bs4 import BeautifulSoup


def current_price(positions):
    for pos in positions:
        url = " https://au.finance.yahoo.com/quote/{}/"
        time.sleep(3)
        ticker = pos.ticker
        if pos.exchange == "ASX":
            ticker += ".AX"

        url = url.format(ticker)
        src = requests.get(url, headers={'User-Agent': 'Custom'}).text
        soup = BeautifulSoup(src, 'lxml')

        print("Getting pricing for {} at {}...".format(ticker, url))

        try:
            s = soup.find('fin-streamer', class_ = "Fw(b) Fz(36px) Mb(-4px) D(ib)")
            pos.set_price(float(s.get('value')))
        except Exception:
            continue

    print()
    return positions