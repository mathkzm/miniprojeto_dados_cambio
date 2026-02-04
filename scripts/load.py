import os
import pandas as pd

DATA_PATH = "../data/cotacoes_dolar.csv"

def load_data_csv(df):
    
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

    df_final = df.drop_duplicates(
        subset=["dataCotacaoDolar"],
        keep="first"
    ).sort_values("dataCotacaoDolar", ascending=True)

    df_final.to_csv(DATA_PATH, index=False)
