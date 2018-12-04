# -*- coding:utf-8 -*-
# 志明
__author__ = '广州医科大学附属第五医院'
__time__ = '2018-11-21 17:15'

import requests as rq

if __name__ == '__main__':
    URL = 'http://192.168.8.63:37777/EaiServer'
    #
    data = u'''<?xml version="1.0" encoding="GB2312"?><DocumentElement>
    <AccessKey>493B312F3B383C34281C130B6ADE4D4E6D0CB8314E5F777C12983DB1F3FB9315902DA23A4847B336AB</AccessKey>
    <MethodName>getCardInfo</MethodName><DataTable><data_org_id>1</data_org_id><data_sys_id>1</data_sys_id><idCardNo>440104198309195010</idCardNo><patientName>邓智韬</patientName></DataTable></DocumentElement>'''
    data = data.encode(encoding='gbk')

    headers = {'Content-Type': 'text/xml'}
    response = rq.post(URL, data=data)
    print('实际编码方式:'+response.encoding)
    response.encoding = r'gbk'
    print('采用编码方式:' + response.encoding)
    print(response.text)
    #
    # print(URL)


