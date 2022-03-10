#!/usr/bin/env python3

import pandas as pd
import numpy as np

from pathlib import Path
from faker import Faker
# from datetime import datetime

from typing import (
    Text
)

from pandas import (
     DataFrame,
     Index
)

DATA_DIR  = "data"
DATA_FILE = "example.csv"

fake = Faker()
Faker.seed()

def get_dataframe(filename: Text) -> DataFrame:
    """
    Returns a pandas dataframe.
    """
    df = DataFrame(pd.read_csv(filename))

    return df

def get_clean_dataframe(df: DataFrame) -> DataFrame:
    """
    Cleans dataframe column names.
    Returns a pandas dataframe.
    """
    clean_df = df

    new_columns = [x.replace("?", "").replace(" ", "_").lower() for x in df.columns]
    clean_df.columns = Index(new_columns)

    return clean_df

def verify_username() -> bool:
    """
    TODO
    """
    ...

def verify_credit_card() -> bool:
    """
    TODO
    """
    ...

def generate_random_data(df: DataFrame) -> None:
    """
    Generates random data
    """

    email = "@smoothceeplusplus.com"

    # Get datasize
    data_size = df.shape[0]
    user_names = np.array([fake.unique.name().replace(" ", "_").lower()+email for _ in range(data_size)], dtype=str)

    df['user'] = user_names

def export_data(df: DataFrame) -> None:
    output_dir = "output"
    output_file = "example.xml"

    if not Path(output_dir).exists():
        Path(output_dir).mkdir()

    df.to_xml(f"{output_dir}/{output_file}")

if __name__ == "__main__":
    file_name = f"{DATA_DIR}/{DATA_FILE}"
    df = get_dataframe(file_name)

    df = get_clean_dataframe(df)

    generate_random_data(df)

    print(df.shape)
    print(df.columns)

    export_data(df)
