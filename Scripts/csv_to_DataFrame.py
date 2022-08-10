import os
import csv
import pandas as pd

def adjust_csv_to_DataFrame(path):
    df = pd.read_csv(path)
    return df


