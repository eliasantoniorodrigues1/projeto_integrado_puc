import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
HTML_DIR = os.path.join(BASE_DIR, 'html')
CREDENTIALS_DIR = os.path.join(BASE_DIR, 'credentials')

# cabecalhos da requisicao do fundamentus
headers = {
    'user-agent': 'insomnia/2022.5.1',
    'cookie': "PHPSESSID=1e088b1b1703a26e7715793d2b60356b",
    'accept': '*/*',
    'content-length': '0'
}
