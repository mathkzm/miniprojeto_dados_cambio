import requests
from datetime import date

def extract_data(data_start, data_end):

    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial='{data_start}'&@dataFinalCotacao='{data_end}'&$top=1000000&$format=json"

    response = requests.get(url)

    response.raise_for_status()

    return response.json()['value']
