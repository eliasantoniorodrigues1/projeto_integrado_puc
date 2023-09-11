from _settings import DATA_DIR
from _yfinance import atualiza_historico_cotacao
from _utils import insert_mysql
from _fundamentus import executa_coleta_fundamentus
from _transform_data import data_processing
from _ibov import insert_empresas_ibov, get_ibov_b3
from _news import get_news


if __name__ == '__main__':
    # opcional: atualiza as empresas no indice do ibov
    # get_ibov_b3()

    # cria a tabela do ibov e insere os valores
    #r = insert_empresas_ibov(table_name='t_indice_ibov_b3')
    #print(r)

    # 1 - atualiza o historico de cotacoes das empresas do ibov
    #atualiza_historico_cotacao()

    
    # 2 - coleta os dados fundamentalistas do site fundamentus
    executa_coleta_fundamentus()

    # 3 - obtem as tabelas do html do site fundamentos e cria as tabelas
    # no banco de dados
    data_processing(file_name='fundamentus.html',
                    table_name='t_fundamentus')
    data_processing(file_name='fundamentus_all_companies.html',
                    table_name='t_fundamentus_all_companies')
    data_processing(file_name='fundamentus_company.html',
                    table_name='t_fundamentus_company')
    
    # 4 - atualiza noticias das empresas do indice
    get_news(table_name='t_ibov_news')
    