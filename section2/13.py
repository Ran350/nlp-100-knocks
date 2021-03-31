import pandas as pd

df1 = pd.read_table("./col1.txt", header=None)
df2 = pd.read_table("./col2.txt", header=None)

merged_df = pd.concat([df1, df2], axis=1)
merged_df.to_csv("./col12.txt", index=False, header=False, sep='\t')
