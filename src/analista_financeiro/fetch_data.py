# fetch_data.py

import yfinance as yf

def get_stock_data(ticker, period='1y', interval='1mo'):
    """
    Busca dados históricos de uma ação específica.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=interval)
    return data
