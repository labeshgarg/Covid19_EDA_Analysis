import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def explore_data(data):
    print("Data Shape:", data.shape)
    print("Data Types:\n", data.dtypes)
    print("Missing Values:\n", data.isnull().sum())
    print("Summary Statistics:\n", data.describe())

    duplicates = data.duplicated().sum()
    print(f"Duplicate rows: {duplicates}")

data_path = 'data/raw/time_series_covid19_confirmed_global.csv'
data = load_data(data_path)
explore_data(data)
