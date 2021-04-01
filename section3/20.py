import json

with open("jawiki-country.json", 'r') as f:
    for line in f:
        df = json.loads(line)
        if df['title'] == 'イギリス':
            text = df['text']
            break

print(text)
