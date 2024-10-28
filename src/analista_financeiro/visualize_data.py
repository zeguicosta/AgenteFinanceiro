import matplotlib.pyplot as plt

def plot_stock_data(data, ticker):
    """
    Plota a variação do preço da ação.
    Retorna a figura para que possa ser manipulada externamente.
    """
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.plot(data.index, data['Close'], label='Preço de Fechamento')
    ax.set_title(f'{ticker} - Variação do Preço da Ação')
    ax.set_xlabel('Data')
    ax.set_ylabel('Preço ($)')
    ax.legend()
    ax.grid(True)
    return fig
