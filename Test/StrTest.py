#!/usr/bin/python3
# -*-encoding:utf-8-*-
__author__ = 'ANDY LIAO'
# 2018-12-02
import re
import timeit as ti


def StrTest(Str, IsASC):
    if len(Str) == 0:
        return '空值'
    Str = Str.split(',')
    Comp= re.compile(r'\d+')
    StrTemp = []
    for item in Str:
        item = item.lstrip().rstrip()
        if Comp.match(item):
            StrTemp.append(item)
    #  字符串数组转int型
    StrTemp = map(int, StrTemp)
    return sorted(StrTemp) if IsASC else sorted(StrTemp, reverse=True)


if __name__ == '__main__':
    Str = '12, 45, 6, 啊, 自己on公司, 中山, 23, 45, 6, 好的'
    print(StrTest(Str, 1))
    # 测试调用函数使用多长时间
    t1 = ti.timeit(stmt="StrTest(Str, IsASC)", setup="from __main__ import  StrTest; Str='12, 45, 6, 啊, 自己on公司, 中山, 23, 45, 6, 好的'; IsASC=1",
                   number=1)

    t2 = ti.repeat(stmt="StrTest(Str, IsASC)",
                   setup="from __main__ import  StrTest; Str='12, 45, 6, 啊, 自己on公司, 中山, 23, 45, 6, 好的'; IsASC=1",
                   repeat=3, number=1000000)
    print(t2)
