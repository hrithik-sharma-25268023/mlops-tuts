"""DVC File 1"""

import pandas as pd
import os

data = {'Name':['Alice', 'Bob', 'Charlie'],
        'Age':[25, 30, 35],
        'City': ['New York', 'Log Angeles', 'Chicago']}

new_row = {'Name':'Cheryl', 'Age':24, 'City':'Dublin'}
new_row_2 = {'Name':'Ana', 'Age':27, 'City':'Galway'}

df = pd.DataFrame(data=data)
df.loc[len(df.index)] = new_row
df.loc[len(df.index)] = new_row_2

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")
