# custom_tool.py

from crewai_tools import BaseTool
from analista_financeiro.fetch_data import get_stock_data
from analista_financeiro.analyze_data import calculate_moving_average, calculate_daily_returns
from analista_financeiro.visualize_data import plot_stock_data, plot_daily_returns
import matplotlib.pyplot as plt
import io
import base64

class AnaliseFinanceira(BaseTool):
    name: str = "Análise Financeira"
    description: str = (
        "Ferramenta para analisar dados financeiros de uma empresa utilizando a API do Yahoo Finance. "
        "Pode buscar dados históricos, calcular médias móveis, retornos diários e gerar visualizações."
    )

    def _run(self, ticker: str) -> str:
        """
        Executa a análise financeira para o ticker fornecido.
        """
        # Obter dados
        data = get_stock_data(ticker)
        if data.empty:
            return "Não foi possível obter os dados da empresa. Verifique o ticker e tente novamente."

        # Analisar dados
        data = calculate_moving_average(data)
        data = calculate_daily_returns(data)

        # Gerar visualizações e converter para base64 para retornar como string
        try:
            fig1 = plot_stock_data(data, ticker)
            buf1 = io.BytesIO()
            fig1.savefig(buf1, format='png')
            buf1.seek(0)
            img_str1 = base64.b64encode(buf1.read()).decode('utf-8')
            plt.close(fig1)

            fig2 = plot_daily_returns(data, ticker)
            buf2 = io.BytesIO()
            fig2.savefig(buf2, format='png')
            buf2.seek(0)
            img_str2 = base64.b64encode(buf2.read()).decode('utf-8')
            plt.close(fig2)

            # Retornar uma resposta que inclui as imagens em base64
            response = (
                f"Análise para {ticker}:\n"
                f"- Média Móvel (20 dias) e Preço de Fechamento:\n"
                f"![Gráfico de Preço de Fechamento](data:image/png;base64,{img_str1})\n\n"
                f"- Retorno Diário:\n"
                f"![Gráfico de Retorno Diário](data:image/png;base64,{img_str2})\n"
            )
            return response
        except Exception as e:
            return f"Ocorreu um erro ao gerar as visualizações: {e}"
