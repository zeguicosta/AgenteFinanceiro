# analyze_data.py

import pandas as pd

def calculate_moving_average(data, window=20):
    """
    Calcula a média móvel dos preços de fechamento.
    """
    data['Moving Average'] = data['Close'].rolling(window=window).mean()
    return data

def calculate_daily_returns(data):
    """
    Calcula os retornos diários da ação.
    """
    data['Daily Return'] = data['Close'].pct_change()
    return data
