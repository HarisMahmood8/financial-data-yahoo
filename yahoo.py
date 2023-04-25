import yfinance as yf
from yahoofinancials import YahooFinancials
import pandas as pd

financial_data = yf.download('TSLA',
                             start='2019-01-01',
                             end='2021-06-12',
                             progress=False,
                             )
with open('tsla_financial_data.txt', 'w') as f:
    print(financial_data.head(), file=f)
