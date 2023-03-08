import requests
from _settings import ibov, project_name, dataset
from _utils import create_bigquery_table
from bs4 import BeautifulSoup
from datetime import datetime as dt
import pprint
import pandas as pd


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
                    'date': dt.today().strftime('%Y-%m-%d %H:%M:%S'),
                    'url': link['href'].replace('/url?q=', ''),
                    'source': source.text.split()[-1],
                    'new': news.text.strip()
                }

                search.append(news)

        # print(f'Total of {len(search)} news founded!')
        # printer.pprint(search)
        df = pd.DataFrame(search)
        print(df.head())
        create_bigquery_table(df=df, dataset_tablename=f'{project_name}.{dataset}.t_news',
                            gcp_project_name=project_name)
    except Exception as e:
        print(e)
        print('Continue...')
        
