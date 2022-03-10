#!/usr/bin/env python3

import matplotlib as plt
import pandas as pd
import numpy as np

from typing import (
    Text
)

from pandas import (
     DataFrame
)

DATA_DIR  = "data"
DATA_FILE = "example.csv"

def get_data(filename: Text) -> DataFrame:
    """
    Returns a pandas dataframe.
    """
    df = pd.read_csv(filename)

    return df

def verify_valid_username() -> bool:
    """
    TODO
    """
    ...
def verify_valid_credit_card() -> bool:
    """
    TODO
    """
    ...
def generate_random_data():
    """
    TODO
    """
    ...

def main() -> None:
    file_name = f"{DATA_DIR}/{DATA_FILE}"
    df = get_data(file_name)

    print(df.shape)

if __name__ == "__main__":
    main()
