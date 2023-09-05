from sqlalchemy import create_engine
import pymysql
import pandas as pd
from _settings import CREDENTIALS_DIR, user, pws, host, port, database
import unicodedata
import re
import os


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(
    CREDENTIALS_DIR, 'consultor-investimentos.json')


def create_bigquery_table(df, dataset_tablename, gcp_project_name, insert_mode='append'):
    '''
        essa funcao cria uma tabela dentro do google bigquery
         params: df: your pandas dataframe
         params: dataset_tablename (str.str): dataset_name.tablename
         params: gcp_project_name: GCP Project ID
    '''
    df.to_gbq(
        destination_table=dataset_tablename,
        project_id=gcp_project_name,
        if_exists=insert_mode,  # 3 available methods: fail/replace/append
        # progressbar=True
    )
    print(f'Tabela {dataset_tablename} criada com sucesso!')
    print(f'Total de linhas inseridas {len(df)}.')


def remove_accents(text: str):
    '''
        funcao para remover acento das palavras
        params: text: texto contendo acentos a serem removidos
        return: texto tratado
    '''
    normalizado = unicodedata.normalize('NFKD', text)
    return ''.join([c for c in normalizado if not unicodedata.combining(c)])


def remove_non_digit(text: str):
    '''
        remove todos os caracteres que nao sao numericos de um texto
        ex: 000.111.666-77 ira retornar 00011166677
        params: text: texto a ser removido caracteres nao numericos
        return: texto tratado
    '''
    return re.sub(r'\D', '', text)


def remove_non_letter(text: str):
    '''
        remove todos os caracteres que nao sao letras e numeros de um texto
        ex: Cotacao-Diaria ira retornar Cotacao_Diaria
        params: text: texto a ser removido caracteres nao numericos
        return: texto tratado
    '''
    new_text = ''
    t = len(text)-1

    for i, char in enumerate(text):
        if i == t and re.match(r'\W', char):
            new_text += re.sub(r'\W', '', char)
        else:
            new_text += re.sub(r'\W', '_', char)

    return re.sub(r'_{2,}', '_', new_text)


def adjust_df_columns(columns: list):
    '''
        essa funcao limpa as colunas contendo 
        caracteres nao permitidos no bigquery
        params: columns: lista contendo todos os cabecalhos de um
        dataframe
        return: lista tratada
    '''
    treated_columns = []
    for name in columns:
        name = remove_accents(name.lower().strip())
        name = remove_non_letter(name)
        treated_columns.append(name)

    return treated_columns


def insert_mysql(data: pd.DataFrame, tbl_name: str):
    conn_string = f'mysql+pymysql://{user}:{pws}@{host}:{port}/{database}'
    sql_engine = create_engine(conn_string, echo=True)
    
    # df = pd.DataFrame(data=dataset)

    conn = sql_engine.connect()
    try:
        frame = data.to_sql(tbl_name, conn, if_exists='fail')
        print(frame)
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(e)        
    else:
        print(f'Table {tbl_name} created successfully.')
    finally:
        conn.close()
