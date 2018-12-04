#!/usr/bin/python3
# -*-encoding:utf-8-*-
__author__ = 'ANDY LIAO'
# 2018-12-02
import re


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