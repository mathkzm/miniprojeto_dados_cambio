import pandas as pd

from extract import extract_data
from transform import transform_data
from load import load_data_csv

data = extract_data()
df = transform_data(data)
load_data_csv(df)

print("Armazenado com sucesso!")