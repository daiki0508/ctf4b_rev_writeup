# ghost 279pt(68solves)

```
A program written by a ghost
```
<br>
<br>
開かれたファイルをエディタで見ると何かしらの構文のような形が見られるが、今まで見たこともない構文のように思われる。<br>

![ghost-1](https://user-images.githubusercontent.com/64737490/82872497-17a30500-9f6e-11ea-9b90-87fb905c058d.png)

ここで、問題文からGhostScriptと検索すると<br><br>

```
Ghostscript（ゴーストスクリプト）は、PostScript や Portable Document Format (PDF) など
アドビシステムズのページ記述言語用のインタプリタおよび、それを基にしたソフトウェアパッケージのことである。
```

と判明。<br>
よってPostScriptの構文構造を調べそれをpythonで表すと、恐らく次のようになると思われる。<br><br>

```python
# -*- coding: utf-8 -*-
flag = ''
output = ''
flag = input('')
if not flag:
    print('I/O Error')
mul = 1
for idx in range(len(flag)):
    get_ord = ord(flag[i])      # ASCIコードを取得
    tmp = get_ord ^ (idx + 1)
    tmp = tmp * mul
    s = 1
    for j in range(463):
        s *= tmp    # s = s * tmp
        s %= 64711  # 剰余計算
    print(s)  # output
    s %= 128
    mul = s + 1
```

<br><br>
そして、ASCIIコードの印字可能文字範囲で1文字ずつoutput.txtの整数値になる文字を探索するソルバーをpythonで書いた。<br><br>

```python
output = '3417 61039 39615 14756 10315 49836 44840 20086 18149 31454 35718 44949 4715 22725 62312 18726 47196 54518 2667 44346 55284 5240 32181 61722 6447 38218 6033 32270 51128 6112 22332 60338 14994 44529 25059 61829 52094'
output = list(map(int, output.split()))     # list(map)で配列の全てにアクセス、.spilit()で文字列を空白文字ごとに配列に分ける。

ans = ''
mul = 1
for idx in range(len(output)):
    for p in range(0x20, 0x7f):     # ASCIコードの印字可能範囲
        get_ord = p
        tmp = get_ord ^ (idx + 1)   # 排他的論理和
        tmp = tmp * mul

        s = 1
        for j in range(463):
            s *= tmp
            s %= 64711
        
        if s == output[idx]:
            print(idx, s, chr(p))
            ans += chr(p)

            s %= 128
            mul = s + 1
            break       # 内側のfor文を抜ける
print('FLAG:', ans)
```
