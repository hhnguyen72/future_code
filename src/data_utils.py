import numpy as np
import pandas as pd
import joblib
from pathlib import Path

from src.constants import CSV_FILE, DROP_COLUMNS, CONVERT_TO_CATEGORICAL, CONVERT_TO_NUMERIC

def load_data(file_path=CSV_FILE):
    """Load data from a CSV file into a pandas DataFrame."""
    print("CSV file Loaded:", file_path)
    return pd.read_csv(file_path)

# def rename_columns(df, rename_map=Column_RENAME_MAP):
    """Rename columns in the DataFrame based on the provided mapping."""
    

def drop_columns(df, columns=DROP_COLUMNS):
    """Drop specified columns from the DataFrame."""
    print("Dropping columns:", columns) 
    return df.drop(columns=columns, errors='ignore')

# def convert_to_categorical(df, columns=CONVERT_TO_CATEGORICAL):
#     """Convert specified columns to categorical dtype."""
#     print("Converting to categorical:", columns)
#     df[columns] = df[columns].astype("str")
#     return df

# def convert_to_numeric(df, columns=CONVERT_TO_NUMERIC):
#     """Convert specified columns to numeric dtype."""
#     print("Converting to numeric:", columns)
#     df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')
#     return df