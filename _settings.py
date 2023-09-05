import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
HTML_DIR = os.path.join(BASE_DIR, 'html')
CREDENTIALS_DIR = os.path.join(BASE_DIR, 'credentials')

# projeto e dataset do google cloud
project_name = 'consultor-investimentos'
dataset = 'raw_data'

# cabecalhos da requisicao do fundamentus
headers = {
    'user-agent': 'insomnia/2022.5.1',
    'cookie': "PHPSESSID=1e088b1b1703a26e7715793d2b60356b",
    'accept': '*/*',
    'content-length': '0'
}

# empresas no índice IBOV
ibov = ['ABEV3', 'AZUL4', 'B3SA3', 'BBAS3', 'BBDC3', 'BBDC4', 'BBSE3',
        'BEEF3', 'BPAC11', 'BRAP4', 'BRDT3', 'BRFS3', 'BRKM5', 'BRML3',
        'BTOW3', 'CCRO3', 'CIEL3', 'CMIG4', 'COGN3', 'CPFE3', 'CRFB3',
        'CSAN3', 'CSNA3', 'CVCB3', 'CYRE3', 'ECOR3', 'EGIE3', 'ELET3',
        'ELET6', 'EMBR3', 'ENBR3', 'ENGI11', 'EQTL3', 'EZTC3', 'FLRY3',
        'GGBR4', 'GNDI3', 'GOAU4', 'GOLL4', 'HAPV3', 'HGTX3', 'HYPE3',
        'IGTA3', 'IRBR3', 'ITSA4', 'ITUB4', 'JBSS3', 'KLBN11', 'LAME4',
        'LREN3', 'MGLU3', 'MRFG3', 'MRVE3', 'MULT3', 'NTCO3', 'PCAR3',
        'PETR3', 'PETR4', 'PRIO3', 'QUAL3', 'RADL3', 'RAIL3', 'RENT3',
        'SANB11', 'SBSP3', 'SULA11', 'SUZB3', 'TAEE11', 'TIMS3', 'TOTS3',
        'UGPA3', 'USIM5', 'VALE3', 'VIVT4', 'VVAR3', 'WEGE3', 'YDUQ3']

# =========================================================================
host = 'localhost'
port = 3306
user = 'root'
pws = 'Matrix*1987'
database = 'projeto_integrado_puc'
