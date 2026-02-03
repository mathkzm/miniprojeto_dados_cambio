#%%
import requests

def extract_data():
    url = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='02-02-2026'&$top=100&$format=json&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao"

    response = requests.get(url)

    response.raise_for_status()

    return response.json()



