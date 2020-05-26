  # -*- coding: utf-8 -*-
s = 'atd4`qdedtUpetepqeUdaaeUeaqau'
s1 = 'c`b bk`kj`KbababcaKbacaKiacki'
ans = ''
for i,j in zip(s, s1):
    ans += chr(ord(i) | ord(j))    # ordでASCIを取得、chrでASCIを文字列にする

print(ans)
