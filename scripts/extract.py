import requests
from datetime import date

def extract_data(data_execucao = None):
    if data_execucao is None:
        data_execucao = date.today().strftime("%m-%d-%Y")

    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data_execucao}'&$top=100&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao"

    response = requests.get(url)

    response.raise_for_status()

    return response.json()['value']
