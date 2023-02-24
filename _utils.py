from sqlalchemy import create_engine
from _settings import CREDENTIALS_DIR
import unicodedata
import re
import os


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(
    CREDENTIALS_DIR, 'consultor-investimentos.json')


def create_bigquery_table(df, dataset_tablename, gcp_project_name, insert_mode='append'):
    # df: your pandas dataframe
    # dataset_tablename (str.str): dataset_name.tablename
    # gcp_project_name: GCP Project ID

    df.to_gbq(
        destination_table=dataset_tablename,
        project_id=gcp_project_name,
        if_exists=insert_mode,  # 3 available methods: fail/replace/append
        # progressbar=True
    )
    print(f'Tabela {dataset_tablename} criada com sucesso!')
    print(f'Total de linhas inseridas {len(df)}.')


def remove_accents(text: str):
    normalizado = unicodedata.normalize('NFKD', text)
    return ''.join([c for c in normalizado if not unicodedata.combining(c)])


def remove_non_digit(text: str):
    return re.sub(r'\D', '', text)


def remove_non_letter(text: str):
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
        this function clear columns chars to
        allow insert into bigquery
    '''
    treated_columns = []
    for name in columns:
        name = remove_accents(name.lower().strip())
        name = remove_non_letter(name)
        treated_columns.append(name)

    return treated_columns


if __name__ == '__name__':
    create_dataset('dados_fundamentalistas', 'us-central1-a')
