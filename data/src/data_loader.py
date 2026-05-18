import pandas as pd
import yaml
from pathlib import Path

def load_config():
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)

def load_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['Date'])
    df['Total_Amount'] = df['Quantity'] * df['Unit_Price']
    df['Month'] = df['Date'].dt.to_period('M')
    return df
