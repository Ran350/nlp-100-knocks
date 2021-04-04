# 国旗画像データが削除されてるか，MediaWikiの仕様変更かなにかで
# Imageinfo APIからurlを取得できないようになっていた:pien:

import re
import json
from pprint import pprint
import requests


def read_article():
    with open("jawiki-country.json", 'r') as f:
        for line in f:
            df = json.loads(line)
            if df['title'] == 'イギリス':
                return df['text']


def extract_info(uk_data):
    pattern = re.compile(
        r'^\{\{基礎情報\s国$(.*?)^\}\}', re.MULTILINE + re.DOTALL)

    return pattern.findall(uk_data)


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


def make_field_dict(template):
    pattern = re.compile(r'\n\|(.+?)(?:\s*)=(?:\s*)(.+?)(?=\n)')

    fields = pattern.findall(template[0])

    return {f[0]: remove_markup(f[1]) for f in fields}


def get_flag_url(image_name):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": "File:" + image_name
    }

    response = requests.get(url=url, params=params)

    pprint(response.json())
    # FIXME: responseにurlが含まれてないよう:pien:


if __name__ == '__main__':
    # Wikipedia記事jsonファイルを読み込む
    uk_data = read_article()

    # 基礎情報テンプレートを抽出
    template = extract_info(uk_data)

    # 各フィールドとその値を抽出
    field = make_field_dict(template)
    # pprint(field)    # ここまでが問題28

    get_flag_url(field['国旗画像'])
