import requests
import pandas as pd
from _settings import ibov, DATA_DIR
from _utils import insert_mysql
import os


def get_ibov_b3():
    '''
      Essa funcao coleta as empresas que compoem o indice
      BOVESPA e retorna um dataset
    '''
    url = 'https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjEyMCwiaW5kZXgiOiJJQk9WIiwic2VnbWVudCI6IjEifQ=='

    try:
        r = requests.get(url)
        data = r.json()['results']
        df = pd.DataFrame(data=data)

        # salva dados coletados
        df.to_csv(os.path.join(DATA_DIR, 'indice_ibov_b3.csv'), index=False)

        return pd.DataFrame(data=data)
    except Exception as e:
        print(f'Error: {e}')
        print('Retornando índice desatualizado...')
        return ibov


def insert_empresas_ibov(table_name):
    df = pd.read_csv(os.path.join(DATA_DIR, 'indice_ibov_b3.csv'))
    insert_mysql(data=df, tbl_name=table_name)

    return 'Empresas do índice atualizadas com sucesso!'
