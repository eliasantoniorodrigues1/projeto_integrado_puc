import pandas as pd
from _settings import HTML_DIR, project_name, dataset
from _utils import create_bigquery_table, adjust_df_columns
import os


def get_data_from_html(file_name: str):
    with open(os.path.join(HTML_DIR, file_name), 'r') as f:
        html = f.read()

    tables = pd.read_html(html)

    return tables[0]


if __name__ == '__main__':
    project_name = project_name
    dataset = dataset
    table_name = 't_companies'
    file_name = 'fundamentus_all_companies.html'

    # cria a tabela no gcp e faz o insert dos dados
    df = get_data_from_html(file_name=file_name)
    header = df.columns.tolist()

    df.columns = adjust_df_columns(header)
    print(df.head())

    create_bigquery_table(df=df, dataset_tablename=f'{dataset}.{table_name}',
                          gcp_project_name=project_name,
                          insert_mode='replace')
