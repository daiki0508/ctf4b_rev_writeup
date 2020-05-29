# Siblangs 363pt(37solves)
```
Well, they look so similar... siblangs.apk
(SHA-1 hash: c08d002c5837ad39d509a1d09ed623003ae97229)
```
<br>
<br>
問題のファイルをダウンロードすると拡張子がapkだと分かる。この拡張子はandroidでしか実行できないので当然このままではファイルを読み取ること
も出来ない。<br>
そこで、apkファイルをjavaファイルに変換して解析を行うことにする。<br>
今回は『unzipコマンド』『dex3jar』『jd-gui』の３つを使った。<br>

## １、apkファイルを解凍
まず最初に、任意のフォルダーにダウンロードしたapkファイルをunzipコマンドで解凍します。<br>

![siblangs01](https://user-images.githubusercontent.com/64737490/83206665-48f91c00-a18c-11ea-99e5-69a0f53f3fbd.png)


すると様々なファイルが表示されたと思います。<br>
今回使うのはこの中にある『classes.dex』というファイルです。この中にはファイルに使われている様々なclass情報が格納されていますが、dexファイル
なのでまだandroidでしか開けません。<br><br>

## ２、dexファイルをjarファイルに変換
そこで、dexファイルをjava形式のjarファイルというものに変換します。(私はここで先ほど居たディレクトリから移動しているので注意!!)<br><br>

```cmd
# sh ./d2j-dex2jar.sh 先ほどのdexファイルパス
```
<br>

![shiblangs02](https://user-images.githubusercontent.com/64737490/83208903-e440c000-a191-11ea-8c6e-e308f9a86b16.png)

すると、『classes-dex2jar.jar』というファイルが新たに出来ていると思います。<br>
これでPCでも読み取ることが出来るjavaのファイルに変換できました。<br><br>

## ３、jd-guiでファイルの中身を見る
このツールは読み込むファイルがzip形式の方が都合が良いので、先ほどのファイル拡張子を.jarから.zipに変えておきましょう。<br>

```cmd
java -jar jd-gui-1.x.x.jar (xの部分はバージョン依存)
```
で、jd-guiを起動してください。<br>
すると、jd-guiが起動してファイル解析を行うことが出来るようになるので、先ほど拡張子を変更しzipファイルにした『classes-dex2jar.zip』を
開いてください。<br><br>

![siblangs03](https://user-images.githubusercontent.com/64737490/83210398-b2c9f380-a195-11ea-845d-b06638fc2a23.png)

すると『ValidateFlagModules』という明らかに怪しいflag処理を見つけることが出来ました。<br>
コードを見た感じだとどうやらこのflagはAES暗号で暗号化されているようなので、pythonのライブラリを使い復号することにします。<br>

```python
from Cryptodome.Cipher import AES

C = [95, -59, -20, -93, -70, 0, -32, -93, -23, 63, -9, 60, 86, 123, -61, -8, 17, -113, -106, 28, 99, -72, -3, 1, -41, -123, 17, 93, -36, 45, 18, 71, 61, 70, -117, -55, 107, -75, -89, 3, 94, -71, 30]
C = "".join(chr(c%256) for c in C)
K = "IncrediblySecure"

aes = AES.new(K, AES.MODE_GCM, C[:12])
print(aes.decrypt(C[12:]))
```

しかし、この暗号だけではflagの後半部分しか入手出来ていません。<br>
ただしflagの最初は【ctf4b】という単語が共通しているので、最初のapkファイルに対してgrepで検索すると<br>

```
flagVal:"ctf4b{",
xored:[34,63,3,77,36,20,24,8,25,71,110,81,64,87,30,33,81,15,39,90,17,27]},
t.handleFlagChange=function(o){
t.setState({flagVal:o})},
                        t.onPressValidateFirstHalf=function(){
                            if("ios"===h.Platform.OS){
                                for(var o="AKeyFor"+h.Platform.OS+"10.3",l=t.state.flagVal,n=0;
                                    n<t.state.xored.length;n++)
                                        if(t.state.xored[n]!==parseInt(l.charCodeAt(n)^o.charCodeAt(n%o.length),10))
                                        return void h.Alert.alert("Validation A Failed","Try again...");
```

というコードがヒットすると思います。(見やすくするためにインデントを調整していますが)<br>
どうやら、flag文字列と『AKeyForios10.3』という文字列をxorした結果がxoredの値になるので、ASCIIコードの印字可能範囲で探索すれば
よさそうです。<br>

```python
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
```

<br>
# あとがき
このwriteupには省略のため載せていませんがここに出てきたツールを初めて使用する方にはツールを用意するのに非常に時間がかかると思います。<br>
しかし、今回のツールは今後もあって困るものではないのでこの機会にぜひダウンロードしておきましょう。
