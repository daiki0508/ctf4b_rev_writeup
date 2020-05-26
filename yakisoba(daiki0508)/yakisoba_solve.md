<h1>yakisoba 156pt (144solves)</h1>

<h2>Would you like to have a yakisoba code?

(Hint: You'd better automate your analysis)</h2>
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
<p>ファイルをダウンロードしてIDAで中身を見ると一見、短いコードに思える。</p><br><br>
(https://user-images.githubusercontent.com/64737490/82852402-dd217400-9f3d-11ea-986e-b460f6e1fea3.png)
<br><br>
しかし、【call sub_820】という部分の詳細を見てみると、600行以上の膨大な比較のコードが記述されている。よって問題文のヒントにもあるように、
オート化して解くべき問題だと推測できる。<br>
有名なツールとして、angrという静的動作解析ツールがあるのでpythonでangrを読み込ませる<br><br>

```python
# -*- coding: utf-8 -*-
import angr
import claripy

def main():
    key_len = 31    # キーの長さを指定(余ったところにはNULL値が入るので適当でよい)
    pj = angr.Project('./yakisoba')   # 解析対象のファイルのパスを指定
    input = claripy.BVS('input', 8*key_len)

    init_state = pj.factory.entry_state(args=['./yakisoba'])
    for b in input.chop(key_len):
        init_state.add_constraints(b != 0)

    sm = pj.factory.simgr(init_state)
    # main
    sm.explore(find=0x4006D2, avoid=[0x4006F7])   # findでたどり着きたい処理(Correct)、avoidで避けたい処理(Wrong)のアドレスを指定
    for f in sm.found:
        print(f.posix.dumps(0))
        print(f.posix.dumps(1))


if __name__ == '__main__':
    main()
```

<br><br>
