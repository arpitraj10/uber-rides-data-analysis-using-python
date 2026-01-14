import pandas as pd

def load_data(path: str):
    """
    Load Uber rides dataset
    """
    df = pd.read_csv(path)
    return df
