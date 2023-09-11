import yfinance as yf
from datetime import datetime, timedelta
from _settings import DATA_DIR
from _utils import adjust_df_columns, insert_mysql
from time import sleep
import os
import pandas as pd


def collect_historical_cotation(ticker: str, period=1095):
    '''
        essa funcao coleta as cotacoes do yfinance dos ultimos tres
        anos
        params: ticker: codigo do papel negociado na bolsa de valores
    '''
    # configurando o espaco de tempo para coleta dos dados na API do yfinance
    delta = timedelta(days=period)  # pega os ultimos tres anos
    yesterday = datetime.today() - timedelta(days=1)  # coleta dados em d-1
    end = yesterday.strftime("%Y-%m-%d")
    start = (yesterday - delta).strftime("%Y-%m-%d")
    data = yf.download(ticker, start=start, end=end)

    # cria a coluna ticker no dataframe
    data['ticker'] = [ticker[:-3] for _ in data.iterrows()]

    # cria a coluna data no inicio do dataframe
    data.insert(0, 'date', '')
    data['date'] = data.index

    # deleta o indice do dataset
    data = data.reset_index(drop=True)

    return data


def atualiza_historico_cotacao():
    df = pd.read_csv(os.path.join(DATA_DIR, 'indice_ibov_b3.csv'))
    tickers_ibov = df['cod'].values.tolist()
    # lista para consolitar todas as coletas
    consolidated = []

    # percorre a lista de empresas listadas no ibov e coleta as
    # cotacoes dos ultimos tres anos e insere no bigquery
    for ticker in tickers_ibov:
        data = collect_historical_cotation(ticker=f'{ticker}.SA')

        # cria a tabela no mysql e faz a insercao dos dados
        tbl_name = 't_historico_cotacoes_ibov'

        # consolida dados coletados
        consolidated.append(data)

        # aguarda um segundo para fazer a proxima requisicao
        sleep(1)

    # salva um backup
    df_consolidated = pd.concat(consolidated)
    df_consolidated.to_csv(
        f'{os.path.join(DATA_DIR, tbl_name)}.csv', index=False)

    # essa funcao coloca o cabecalho em caixa baixa e remove todos
    # os caracteres especiais para possibilitar a insercao no
    # bigquery
    columns = adjust_df_columns(columns=df_consolidated.columns.tolist())
    df_consolidated.columns = columns

    print(df_consolidated.head())

    # executa insert no banco de dados
    insert_mysql(data=df_consolidated, tbl_name=tbl_name, if_exists_action='append')

    print('Histórico de contações atualizado com sucesso!')
    
