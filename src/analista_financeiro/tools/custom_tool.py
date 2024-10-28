from crewai_tools import BaseTool
from analista_financeiro.fetch_data import get_stock_data
from analista_financeiro.visualize_data import plot_stock_data
import matplotlib.pyplot as plt
import io
import base64

class AnaliseFinanceira(BaseTool):
    name: str = "Análise Financeira"
    description: str = (
        "Ferramenta para analisar dados financeiros de uma empresa utilizando a API do Yahoo Finance. "
        "Pode buscar dados históricos e gerar visualizações da variação do preço da ação."
    )

    def _run(self, ticker: str) -> str:
        """
        Executa a análise financeira para o ticker fornecido.
        """
        # Obter dados
        data = get_stock_data(ticker)
        if data.empty:
            return "Não foi possível obter os dados da empresa. Verifique o ticker e tente novamente."

        # Gerar visualização e converter para base64
        try:
            # Plotar a variação do preço da ação
            fig = plot_stock_data(data, ticker)
            buf = io.BytesIO()
            fig.savefig(buf, format='png')
            buf.seek(0)
            img_str = base64.b64encode(buf.read()).decode('utf-8')
            plt.close(fig)

            # Converter os dados obtidos em texto
            data_text = data.to_string()

            # Retornar a resposta com o texto dos dados e o gráfico
            response = (
                f"Análise para {ticker}:\n\n"
                f"**Dados obtidos da API:**\n```\n{data_text}\n```\n"
                f"**Variação do Preço da Ação:**\n"
                f"![Gráfico de Variação do Preço](data:image/png;base64,{img_str})\n"
            )
            return response
        except Exception as e:
            return f"Ocorreu um erro ao gerar as visualizações: {e}"
