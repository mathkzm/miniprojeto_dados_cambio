import os
import pandas as pd

DATA_PATH = "../data/cotacoes_dolar.csv"

def load_data_csv(df):
    
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

    if os.path.exists(DATA_PATH):
        df_existing = pd.read_csv(DATA_PATH)
        df_final = pd.concat([df_existing, df], ignore_index=True)
        df_final = df_final.drop_duplicates(
            subset=["dataCotacaoDolar"],
            keep="first"
        )
    else:
        df_final = df

    df_final = df_final.sort_values("dataCotacaoDolar", ascending=True)
    df_final.to_csv(DATA_PATH, index=False)
