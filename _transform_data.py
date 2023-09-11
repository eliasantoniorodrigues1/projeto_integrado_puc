import pandas as pd
from _settings import HTML_DIR, project_name, dataset
from _utils import insert_mysql, adjust_df_columns
import os


def get_data_from_html(file_name: str):
    with open(os.path.join(HTML_DIR, file_name), 'r') as f:
        html = f.read()

    tables = pd.read_html(html)

    return tables[0]


def data_processing(file_name, table_name):
    # project_name = project_name
    # dataset = dataset
    # table_name = 't_companies'
    # file_name = 'fundamentus_all_companies.html'

    # cria a tabela no gcp e faz o insert dos dados
    df = get_data_from_html(file_name=file_name)
    header = df.columns.tolist()

    df.columns = adjust_df_columns(header)
    print(df.head())

    # create_bigquery_table(df=df, dataset_tablename=f'{dataset}.{table_name}',
    #                      gcp_project_name=project_name,
    #                      insert_mode='replace')
    insert_mysql(data=df, tbl_name=table_name, if_exists_action='append')
