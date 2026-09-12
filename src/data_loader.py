import pandas as pd
from src.config import RAW_DATA_PATH


def load_data():
    df = pd.read_csv(
        RAW_DATA_PATH
    )

    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" " , "_" , regex=False)
    )
    return df


