import sys
import pandas as pd

pn_df = pd.read_table("./popular-names.txt", header=None, sep='\t')

length = len(pn_df)
skip = int(length / int(sys.argv[1]))

dfs = [pn_df.loc[i:i+skip-1, :] for i in range(0, length, skip)]

for i, df in enumerate(dfs):
    df.to_csv(f"./popular-names{i}.txt",
              sep='\t',
              index=False,
              header=False)
