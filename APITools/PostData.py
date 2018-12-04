#!/usr/bin/python3
# -*-encoding:utf-8-*-
__author__ = 'ANDY LIAO'
# 2018-11-24
import requests as rq

class PostData:

    def __init__(self, URL, Data):
        self.URL = URL
        self.Data = Data

    def getData(self):
        try:
            reponse = rq.post(self.URL, data=self.Data, timeout=0.5)
            reponse.encoding = r'gbk'
            return reponse.text
        except:
            print('ERROR')
        finally:
            return '网络异常'

