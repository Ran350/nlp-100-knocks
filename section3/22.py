import re
import json

with open("jawiki-country.json", 'r') as f:
    for line in f:
        df = json.loads(line)
        if df['title'] == 'イギリス':
            uk_data = df['text']
            break


pattern = re.compile(r'\[\[Category:(.*?)(\|.*)?\]\]')
categories = pattern.finditer(uk_data)

print([c.group(1) for c in categories])
