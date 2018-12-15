# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 广医五院  志明  2018-12-10 16:51
# 当前计算机登录名称 :广州医科大学附属第五医院
# 项目名称  :
# 编译器   :PyCharm
__author____ = '志明'
__time__ = '2018-12-10 '


import pymssql


if __name__ == '__main__':
    '''使用pymssql出现问题,估计是python解析器的问题'''
    print(dir(pymssql))
    conn = pymssql.connect('172.16.230.100', 'sa', 'sql', 'mz_patient')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM mz_patient WHERE p_id=%d%', '15')

    for row in cursor:
        print(row)

    cursor.close()
    conn.close()
