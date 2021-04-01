from os import sep
import pandas as pd

df = pd.read_table("popular-names.txt", header=None, sep='\t')

df.sort_values(by=2, ascending=False, inplace=True)

print(df)
