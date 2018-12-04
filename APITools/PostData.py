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
            reponse = rq.post(self.URL, data=self.Data.encode(encoding='gbk'))
            reponse.encoding = r'gbk'
            return reponse.text
        except:
            return '网络超时或者网络异常!'
        # finally:
        #     return '网络异常'


if __name__ == '__main__':
    url = r'http://192.168.8.63:37777/EaiServer'
    data = r'''<?xml version="1.0" encoding="GB2312"?><DocumentElement><AccessKey>493B312F3B383C34281C130B6ADE4D4E6D0CB8314E5F777C12983DB1F3FB9315902DA23A4847B336AB</AccessKey><MethodName>HqWxPayService</MethodName><DataTable><FunctionName>WX_MzHuaJia</FunctionName><PatientID>000019208200</PatientID><mzFeeIdList>12</mzFeeIdList><Response_type>02</Response_type><ZG_YB_FLAG></ZG_YB_FLAG><ybMapFlag>1</ybMapFlag><psOrdNum></psOrdNum></DataTable></DocumentElement>
'''
    print(url)
    # print(data)
    print(PostData(url, data).getData())
