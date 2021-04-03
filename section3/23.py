import re
import json

with open("jawiki-country.json", 'r') as f:
    for line in f:
        df = json.loads(line)
        if df['title'] == 'イギリス':
            uk_data = df['text']
            break


lv1_pattern = re.compile(r'^={2}([^=]+)={2}$', re.MULTILINE)
lv2_pattern = re.compile(r'^={3}([^=]+)={3}$', re.MULTILINE)
lv3_pattern = re.compile(r'^={4}([^=]+)={4}$', re.MULTILINE)

lv1_categories = lv1_pattern.findall(uk_data)
lv2_categories = lv2_pattern.findall(uk_data)
lv3_categories = lv3_pattern.findall(uk_data)

print("レベル1：", lv1_categories)
print("レベル2：", lv2_categories)
print("レベル3：", lv3_categories)
