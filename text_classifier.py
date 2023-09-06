import numpy as np
import pandas as pd


def file_reader(filename):
    df = pd.read_csv(filename)

    return df

filename = "spam.csv"
email_data = file_reader(filename)
