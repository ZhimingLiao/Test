#!/usr/bin/python3
# -*-encoding:utf-8-*-
__author__ = 'ANDY LIAO'
# 2018-11-25
import os
import datetime


def LogWrite(StrInput, StrOutput):
    FileDir = r'日志文件'
    if os.path.isdir(FileDir) is False:
        os.mkdir(FileDir)
    FileName = os.path.join(FileDir, datetime.datetime.now().strftime('%Y-%m-%d')+r'.txt')
    with open(FileName, 'a+') as fp:
        fp.writelines(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\t入参和出参日志:')
        fp.write('\n')
        fp.writelines('*'*15+'以下是入参'+'*'*15)
        fp.write('\n')
        fp.writelines(StrInput)
        fp.write('\n')
        fp.writelines(StrOutput)
        fp.write('\n')
        fp.writelines('*'*15+'以上是入参'+'*'*15)
        fp.write('\n\n')


if __name__ == '__main__':
    print(os.getcwd())
    LogWrite('a', 'b')

