import pandas as pd

from extract import extract_data
from transform import transform_data
from load import load_data_csv

print("Informe a data no formato MM-DD-YYYY")

data_inicio = input("Informe a data de início: ")
data_fim = input("Informe a data de fim: ")

data = extract_data(data_inicio,data_fim)
df = transform_data(data)
load_data_csv(df)

print("Armazenado com sucesso!")