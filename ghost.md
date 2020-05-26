<h1>ghost 279pt(68solves)</h1>

<h2>A program written by a ghost</h2>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
開かれたファイルをエディタで見ると何かしらの構文のような形が見られるが、今まで見たこともない構文のように思われる。<br>
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
    get_ord = ord(flag[i])
    tmp = get_ord ^ (idx + 1)
    tmp = tmp * mul
    s = 1
    for j in range(463):
        s *= tmp
        s %= 64711
    print(s)  # output
    s %= 128
    mul = s + 1
```
