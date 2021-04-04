import re
import json

with open("jawiki-country.json", 'r') as f:
    for line in f:
        df = json.loads(line)
        if df['title'] == 'イギリス':
            uk_data = df['text']
            break


pattern = re.compile(r'\[\[ファイル:(.+?\.[a-zA-Z]+?)\|')

categories = pattern.findall(uk_data)

print(categories)
