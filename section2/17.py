import pandas as pd

df = pd.read_table("./popular-names.txt", sep='\t', header=None)

print(sorted(df[0].unique()))
