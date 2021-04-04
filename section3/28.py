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
    r'^\{\{基礎情報\s国$(.*?)^\}\}', re.MULTILINE + re.DOTALL)

template = template_pattern.findall(uk_data)


def remove_markup(field):
    # 強調マークアップ
    field = re.compile(r'\'{2,5}').sub(r'', field)

    # 内部リンク
    field = re.compile(r'\[\[(.+?)\]\]').sub(r'\1', field)

    # 外部リンク
    field = re.compile(r'\[.*?\]').sub(r'', field)

    # テンプレート
    field = re.compile(r'\{\{.*?\}\}').sub(r'', field)

    # htmlタグ
    return re.compile(r'<.+?>').sub(r'', field)


# 各フィールドとその値を抽出
pattern = re.compile(r'\n\|(.+?)(?:\s*)=(?:\s*)(.+?)(?=\n)')

field_list = pattern.findall(template[0])

field_dict = {f[0]: remove_markup(f[1]) for f in field_list}

pprint(field_dict)
