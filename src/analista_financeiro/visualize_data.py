# visualize_data.py

import matplotlib.pyplot as plt

def plot_stock_data(data, ticker):
    """
    Plota o preço de fechamento e a média móvel.
    Retorna a figura para que possa ser manipulada externamente.
    """
    fig, ax = plt.subplots(figsize=(14,7))
    ax.plot(data['Close'], label='Preço de Fechamento')
    if 'Moving Average' in data.columns:
        ax.plot(data['Moving Average'], label='Média Móvel')
    ax.set_title(f'{ticker} - Preço de Fechamento e Média Móvel')
    ax.set_xlabel('Data')
    ax.set_ylabel('Preço ($)')
    ax.legend()
    ax.grid(True)
    return fig

def plot_daily_returns(data, ticker):
    """
    Plota os retornos diários da ação.
    Retorna a figura para que possa ser manipulada externamente.
    """
    fig, ax = plt.subplots(figsize=(14,7))
    ax.plot(data['Daily Return'], label='Retorno Diário')
    ax.set_title(f'{ticker} - Retorno Diário')
    ax.set_xlabel('Data')
    ax.set_ylabel('Retorno (%)')
    ax.legend()
    ax.grid(True)
    return fig
