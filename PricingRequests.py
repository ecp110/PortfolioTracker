from asyncore import write
from datetime import date
from termios import VEOL
import requests
from Utilities import date_to_yh
from bs4 import BeautifulSoup


url = " https://au.finance.yahoo.com/quote/{}/history?period1={}&period2={}&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true"
# URL needs to be formatted with: ticker, start date, end date

start_date = date_to_yh(1, 1, 2021)
end_date = date_to_yh(1, 1, 2022)
ticker = "VAS.AX"

url = url.format(ticker, start_date, end_date)
src = requests.get(url, headers={'User-Agent': 'Custom'}).text
soup = BeautifulSoup(src, 'lxml')

s = soup.find_all('td', class_ = "Py(10px) Pstart(10px)")
info = []
x = 0
while x < len(s) - 5:
    open = s[x].text
    x += 1

    high = s[x].text
    x += 1

    low = s[x].text
    x +=1

    close = s[x].text
    x +=1

    adjclose = s[x].text
    x += 1

    vol = s[x].text
    x += 1

    info.append([open, high, low, close, adjclose, vol])

print(['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'])
for row in info:
    print(row)