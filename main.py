from _utils import insert_mysql
from _utils import adjust_df_columns
from _settings import ibov, DATA_DIR
from _yfinance import collect_historical_cotation
from time import sleep
import pandas as pd
import os


if __name__ == '__main__':
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

    # drop index
    df_consolidated.drop(0)
    print(df_consolidated.head())

    # executa insert no banco de dados
    insert_mysql(data=df_consolidated, tbl_name=tbl_name)
