# 第4章 形態素解析

## Build

### ファイルの準備
[吾輩は猫である](https://nlp100.github.io/data/neko.txt) をダウンロードして，section4ディレクトリに配置してね

または次のコマンドを実行してね
```sh
wget https://nlp100.github.io/data/neko.txt
```

### MeCabの準備
MeCabの環境構築をしてね．
[MecabをPythonで使うまで](https://qiita.com/Sak1361/items/47e9ec464ccc770cd65c) が参考になるよ

## neko.txt.mecab の用意
```sh
mecab -o neko.txt.mecab neko.txt
```

