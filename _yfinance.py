import yfinance as yf
from datetime import datetime, timedelta
from _settings import ibov, project_name, dataset
from _utils import create_bigquery_table, adjust_df_columns
from time import sleep


def collect_historical_cotation(ticker: str):
    '''
        essa funcao coleta as cotacoes do yfinance dos ultimos tres
        anos
        params: ticker: codigo do papel negociado na bolsa de valores
    '''
    # configurando o espaco de tempo para coleta dos dados na API do yfinance
    delta = timedelta(days=1095)  # pega os ultimos tres anos
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


if __name__ == '__main__':
    # percorre a lista de empresas listadas no ibov e coleta as
    # cotacoes dos ultimos tres anos e insere no bigquery
    for ticker in ibov[:-1]:
        data = collect_historical_cotation(ticker=f'{ticker}.SA')

        # essa funcao coloca o cabecalho em caixa baixa e remove todos
        # os caracteres especiais para possibilitar a insercao no
        # bigquery
        columns = adjust_df_columns(columns=data.columns.tolist())
        data.columns = columns

        # cria a tabela no gcp e faz a insercao dos dados
        table_name = 't_historico_cotacoes_ibov'
        create_bigquery_table(
            df=data, dataset_tablename=f'{dataset}.{table_name}',
            gcp_project_name=project_name, insert_mode='append'
        )

        # aguarda um segundo para fazer a proxima requisicao
        sleep(1)
