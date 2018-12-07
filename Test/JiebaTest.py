# -*- coding:utf-8 -*-
# 志明
__author__ = '广州医科大学附属第五医院'
__time__ = '2018-11-26 7:58'
import jieba as jb

if __name__ == '__main__':
    StrTest = '''亲爱的用户您好感谢您使用百度服务。您正在进行邮箱验证，请在验证码输入框中输入此次验证码：
    663526 以完成验证。如非本人操作，请忽略此邮件，由此给您带来的不便请谅解！'''
    a = jb.cut(StrTest, cut_all=True)
    # import re
    # 正则使用的标点符号
    # StrRE = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'
    # ReCompile = re.compile(StrRE)
    # Result = list()
    # b = list(a)
    # for item in range(len(b)):
    #     if ReCompile.findall(b[item]) is not None and b[item] != '':
    #         Result.append(b[item])
    # print(Result)

    # 默认启用了HMM（隐马尔科夫模型）进行中文分词，实际效果不错
    # 全屏模式
    # jb.add_word('忽略此') #添加词汇
    # jb.enable_parallel() 启用平行计算
    Result = jb.cut(StrTest, cut_all=True)
    # Result只能使用一次
    ListData = list(Result)
    # 精简模式,默认模式
    # Result = jb.cut(StrTest, cut_all=False)
    # print(list(Result))
    # # 搜索引擎模式
    # Result = jb.cut_for_search(StrTest)
    # print(list(Result))
    temp = dict()

    print(ListData)
    for item in ListData:
        # temp[item]+=1 if (item in temp) else (temp[item]=1)
        if item in temp:
            temp[item] += 1
        else:
            temp[item] = 1
    # print(type(temp.keys()))
    # print(sorted(temp.keys(), reverse=True))
    # print(temp)
    # print(list(temp))
    # Json
    # 模块提供了四个方法： dumps、dump、loads、load
