# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 广医五院  志明  2018-12-06 19:58
# 当前计算机登录名称 :广州医科大学附属第五医院
# 项目名称  :
# 编译器   :PyCharm
__author____ = '志明'
__time__ = '{2018-12-06} '


class ClassTest(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.__age = age
        self.sex = sex

    # 设置属性值
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


if __name__ == '__main__':
    test = ClassTest(name='张三', age=18, sex='男')
    test.age = 30
    print(test.age)
    test.doTest = lambda x, y:(x+y)
    print(test.doTest(4, 5))
