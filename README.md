# MPFILE TO TEXT
音声・録画ファイル(MP3, MP4, Wav)をテキストに変換する事ができます。

## 初回セットアップ
pythonの実行環境が用意されていることをかくにんしてください。

```python
pip install moviepy
pip install faster_whisper
```

## 実行
変換元のファイルはmain.pyと同じ階層のディレクトリに配置し、以下のコマンドを実行してください。

```python
python main.py
```

実行結果のテキストファイルはoutputディレクトリ配下に出力されます。
すでに一度実行されて、outputが出力されている音声ファイルについては、実行がスキップされます。
outputファイルを削除すると再度実行可能なので、再実行の際はファイルを削除してください。