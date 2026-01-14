import pandas as pd

def preprocess_data(df: pd.DataFrame):
    """
    Clean and preprocess data
    """
    df['START_DATE'] = pd.to_datetime(df['START_DATE'], errors='coerce')
    df['END_DATE'] = pd.to_datetime(df['END_DATE'], errors='coerce')

    df['HOUR'] = df['START_DATE'].dt.hour
    df['DAY'] = df['START_DATE'].dt.day_name()
    df['MONTH'] = df['START_DATE'].dt.month_name()

    df['PURPOSE'].fillna('Unknown', inplace=True)

    return df
