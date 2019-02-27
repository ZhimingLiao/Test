# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 2019-01-29 08:13 广医五院  ANDY
# 当前计算机登录名称 :广州医科大学附属第五医院
# 项目名称  :
# 编译器   :PyCharm
import pymssql
import os

__author____ = '志明'
__time__ = '2019-01-29 08:13'

'''
读取数据库数据,将数据库数据封装到文本文件中
'''

def WriteData(ContentStr='', FileName='', FileDir='Temp'):
        if not os.path.exists((FileDir)):
            os.makedirs(FileDir)
        File = os.path.join(FileDir, FileName)
        File = File.replace(u"\r", "").replace(u"\n", "")
        ContentStr = ContentStr.replace(u"\r\n\r\n", u"\r\n")
        with open(File, 'w+', encoding='utf-8') as file:
            print(File)
            try:
                file.write(ContentStr)
            except Exception:
                print('写入文件时发现异常!')


if __name__ == '__main__':
    conn = pymssql.connect(host='172.16.230.32', user='sa', password='sql', database='HQEAI')
    Cur = conn.cursor()
    DataList = None
    if not Cur:
        print("链接数据库失败")
    else:
        print("链接数据库成功!")
        Cur.execute("select  SERVICE_NAME, SQL_TEXT, HELP_TEXT from EAI_SERVICE_LIST where SQL_TEXT is not null")
        DataList = Cur.fetchall()
        if DataList:
            for data in DataList:
                WriteData(ContentStr=data[1], FileName=data[0]+"("+data[2]+").sql", FileDir=u'日志')
    Cur.close()