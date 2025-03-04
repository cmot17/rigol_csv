import csv
import pandas as pd
from typing import Tuple

def read_rigol_csv(csv_file_name: str) -> Tuple[pd.DataFrame, float, float]:
    """
    Reads a Rigol oscilloscope CSV file and returns the waveform data along with timing information.
    
    Parameters:
        csv_file_name (str): Path to the CSV file.
    
    Returns:
        tuple: (data (DataFrame), t0 (float), dT (float))
    
    Raises:
        ValueError: If the CSV file cannot be read or is malformed.
    """
    with open(csv_file_name) as f:
        rows = list(csv.reader(f))
        i = 0
        while rows[0][i] != "":
            i += 1
        numcols = i - 2
        t0 = float(rows[1][numcols])
        dT = float(rows[1][numcols + 1])
    
    data: pd.DataFrame = pd.read_csv(csv_file_name, usecols=range(0, numcols), skiprows=[1])
    data['X'] = t0 + data['X'] * dT
    return data, t0, dT