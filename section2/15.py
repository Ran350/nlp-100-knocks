import sys
import pandas as pd

df = pd.read_table("./popular-names.txt", header=None, sep='\t')

line = int(sys.argv[1])
print(df.tail(line))
