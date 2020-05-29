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
