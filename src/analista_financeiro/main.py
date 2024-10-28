#!/usr/bin/env python
from analista_financeiro.crew import AnalistaFinanceiroCrew

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'ticker': 'CMIG4.SA'  # Ticker da empresa (ex: 'AAPL' para Apple, 'BBAS3.SA' para Banco do Brasil)
    }
    AnalistaFinanceiroCrew().crew().kickoff(inputs=inputs)