#!/usr/bin/env python3

import pandas as pd

# Specify tab ('\t') as the delimiter
df = pd.read_csv("0039102-231002084531237.csv", delimiter='\t')

print(df.head())  # Displays the first few rows
print(df.columns)  # Displays the field names (headers)

