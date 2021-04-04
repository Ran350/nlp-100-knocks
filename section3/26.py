import re
import json
from pprint import pprint

with open("jawiki-country.json", 'r') as f:
    for line in f:
        df = json.loads(line)
        if df['title'] == 'イギリス':
            uk_data = df['text']
            break


# 基礎情報テンプレートを抽出
template_pattern = re.compile(
    r'^\{\{基礎情報\s国$(.*?)^\}\}',
    re.MULTILINE + re.DOTALL)

template = template_pattern.findall(uk_data)
# print(template)


# 各フィールドとその値を抽出
pattern = re.compile(r'\n\|(.+?)(?:\s*)=(?:\s*)(.+?)\n')

field_list = pattern.findall(template[0])

field_dict = {
    f[0]:
    f[1].replace("\'\'\'\'\'", "").replace("\'\'\'", "").replace("\'\'", "")
    for f in field_list
}

pprint(field_dict)
