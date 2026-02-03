#%%
import pandas as pd
from extract import extract_data


data = extract_data()


def transform_data(data):
    df = pd.DataFrame(data)

    df["dataHoraCotacao"] = pd.to_datetime(df["dataHoraCotacao"]).dt.strftime("%Y-%m-%d %H:%M:%S")

    df["cotacaoCompra"] = df["cotacaoCompra"].astype(float)

    df["cotacaoVenda"] = df["cotacaoVenda"].astype(float)

    df = df.rename(columns={"dataHoraCotacao":"dataCotacaoDolar",
    "cotacaoCompra":"cotacaoCompraDolar",
    "cotacaoVenda":"cotacaoVendaDolar"})

    return df
