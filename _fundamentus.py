from _settings import HTML_DIR
import os
import http.client
from time import sleep
from _settings import headers


def get_fundamentus_data(base_url: str, url: str, file_name: str):
    conn = http.client.HTTPSConnection(base_url)
    payload = ''

    conn.request('POST', url, payload, headers)

    res = conn.getresponse()
    data = res.read()

    html_data = data.decode('latin-1')

    with open(os.path.join(HTML_DIR, file_name), 'w') as f:
        f.write(html_data)

    print(f'Dados coletado com sucesso e salvos em {file_name}')


if __name__ == '__main__':
    base_url = 'www.fundamentus.com.br'
    url_fundamentos = '/resultado.php'
    url_list_companies = '/detalhes.php?papel='
    url_company = '/detalhes.php?papel=AALR3'

    get_fundamentus_data(
        base_url=base_url, url=url_fundamentos, file_name='fundamentos.html')
    sleep(3)
    get_fundamentus_data(base_url=base_url, url=url_list_companies,
                         file_name='fundamentus_all_companies.html')
    sleep(3)
    get_fundamentus_data(base_url=base_url, url=url_fundamentos,
                         file_name='fundamentus_company.html')
