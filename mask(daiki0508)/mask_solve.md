# mask 62pt(354solve)

## The price of mask goes down. So does the point (it's easy)!

## (SHA-1 hash: c9da034834b7b699a7897d408bcb951252ff8f56)
<br>
<br>
長々と説明文が書いてあるが問題文は全く関係ない。<br>
ダウンロードしたファイルを解凍して開き、fileコマンドを開くとx86/x64のELF形式のファイルだと分かる。よって、IDAでファイルの中身を見てみる。

<br><br>
![mask_ida-2](https://user-images.githubusercontent.com/64737490/82870883-a3fff880-9f6b-11ea-8edf-894bfc787027.jpg)
<br><br>
 
すると中には二つの文字列がそれぞれレジスタにleaされていると分かる。また、
<br><br>
![mask_ida-3](https://user-images.githubusercontent.com/64737490/82871049-e3c6e000-9f6b-11ea-9f71-450319ba0dce.jpg)
<br><br>
  この画像から、指定したFLAG文字列を0x75でAND演算した文字列、0xEBでAND演算した文字列がそれぞれ１つ目の画像の結果になるかどうかで正しいFLAGか判断していると思う。(test eax eaxより）
  <br>
  よって、以下のpythonコードで解析を行う。<br><br>
  
```python
  # -*- coding: utf-8 -*-
s = 'atd4`qdedtUpetepqeUdaaeUeaqau'
s1 = 'c`b bk`kj`KbababcaKbacaKiacki'
ans = ''
for i,j in zip(s, s1):
    ans += chr(ord(i) | ord(j))    # ordでASCIを取得、chrでASCIを文字列にする

print(ans)
```
