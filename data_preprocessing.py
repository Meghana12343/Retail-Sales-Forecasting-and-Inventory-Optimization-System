import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df.dropna(inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    return df
