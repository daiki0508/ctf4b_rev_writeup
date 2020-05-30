# flagの前半部分
# coding: utf-8 -*-
flagVal = 'ctf4b{'
xored = [34,63,3,77,36,20,24,8,25,71,110,81,64,87,30,33,81,15,39,90,17,27]
ios = 'AKeyForios10.3'

ans = ''
for i in range(len(flagVal), len(xored)):
    print(i)
    for f in range(0x20, 0x7e):   # ASCIIコード印字可能範囲を指定
        t = f ^ ord(ios[i % len(ios)])    # ASCIIコードを取得
        if t == xored[i]:
            print(i, t, chr(f))   # ASCIIコードを文字列に変換
            ans += chr(f)
            break
print(flagVal + ans)
