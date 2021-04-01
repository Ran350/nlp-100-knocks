import pandas as pd

df = pd.read_table("popular-names.txt", header=None, sep='\t')

print(df[0].value_counts(ascending=False))
