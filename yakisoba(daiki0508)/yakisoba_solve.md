# yakisoba 156pt (144solves)

```
Would you like to have a yakisoba code?
(Hint: You'd better automate your analysis)
```
<br>
<br>

ファイルをダウンロードしてIDAで中身を見ると一見、短いコードに思える。<br><br>

![yakisoba-1](https://user-images.githubusercontent.com/64737490/82873050-e2e37d80-9f6e-11ea-8970-06777dca8bc1.png)
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
