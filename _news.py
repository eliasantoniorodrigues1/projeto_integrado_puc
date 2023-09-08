import requests
from _settings import ibov, DATA_DIR
from _utils import insert_mysql, execute_query
from bs4 import BeautifulSoup
from datetime import datetime as dt
import pandas as pd
from sqlalchemy.sql import text
import os


def get_tickers_ibov():
    query = text('SELECT cod FROM projeto_integrado_puc.t_indice_ibov_b3')
    df = execute_query(query=query)
    ibov_atualizado = df['cod'].values.tolist()

    return ibov_atualizado


def get_news(table_name: str):
    # atualiza as empresas no indice ibov
    ibov_atualizado = get_tickers_ibov()

    if len(ibov_atualizado) > 0:
        ibov = ibov_atualizado.copy()

    for ticker in ibov:
        try:
            url = f'https://www.google.com/search?q={ticker}&source=lnms&tbm=nws&sa=X&ved=2ahUKEwi2n6rT-sr9AhUmKbkGHcS7AfMQ_AUoAnoECAEQBA&biw=1920&bih=929&dpr=1'

            r = requests.get(url)

            soup = BeautifulSoup(r.text, 'html.parser')
            links = soup.find_all('a', href=True)
            search = []
            for link in links:
                news = link.find('h3')
                source = link.find('div')

                if news and link:
                    news = {
                        'ticker': ticker,
                        'creation_date': dt.today().strftime('%Y-%m-%d %H:%M:%S'),
                        'url': link['href'].replace('/url?q=', ''),
                        'source': source.text.split()[-1],
                        'news': news.text.strip()
                    }

                    search.append(news)

            '''
            statement = text("""
                INSERT INTO projeto_integrado_puc.t_news_ibov(
                      ticker
                    , creation_date
                    , url
                    , source
                    , news) 
                    VALUES(:ticker, :creation_date, :url, :source, :news);
                    """)
            execute_query(statement, search)
            '''
            print(f'Total of {len(search)} news founded!')
            # printer.pprint(search)
            df = pd.DataFrame(search)
            # df = df.reset_index(drop=True)
            # print(df.head())
            # create_bigquery_table(df=df, dataset_tablename=f'{project_name}.{dataset}.t_news',
            #                     gcp_project_name=project_name)

            # save csv file
            df.to_csv(os.path.join(DATA_DIR, f'{table_name}.csv'), index=False)
            # insert mysql
            insert_mysql(data=df, tbl_name='t_news_ibov', if_exists_action='append')

        except Exception as e:
            print(e)
            print('Continue...')


if __name__ == '__main__':
    get_news('t_news_ibov')
