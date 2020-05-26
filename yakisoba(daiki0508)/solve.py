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
