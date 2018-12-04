# -*- coding:utf-8 -*-
# 志明
__author__ = '广州医科大学附属第五医院'
__time__ = '2018-11-25 0:51'

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
        reponse = rq.post(self.URL, data=self.Data)
        reponse.encoding = r'gbk'
        return reponse.text


if __name__ == '__main__':
    url = '''<?xml version="1.0" encoding="GB2312"?>
<DocumentElement>
	<AccessKey>493B312F3B383C34281C130B6ADE4D4E6D0CB8314E5F777C12983DB1F3FB9315902DA23A4847B336AB</AccessKey>
	<MethodName>HqWxPayService</MethodName>
	<DataTable>
		<FunctionName>WX_MzShouFei</FunctionName>
		<PatientID>000019212300</PatientID>
		<mzFeeIdList>11</mzFeeIdList>
		<Response_type>02</Response_type>
		<payTime>2018-11-14 17:12:16</payTime>
		<payMode>AliPay</payMode>
		<psOrdNum>2018110922001434221008254568</psOrdNum>
		<ybMapFlag>1</ybMapFlag>
		<agtCode>ZFB01</agtCode>
		<ChargeTotal>1234</ChargeTotal>
		<ChargeYb>104</ChargeYb>
		<ChargePay>1130</ChargePay>
		<YbCardBalance></YbCardBalance>
		<ChargeOtherPay>1130</ChargeOtherPay>
	</DataTable>
</DocumentElement>'''
    print(PostData('http://172.16.230.100:37777/EaiServer', url).getData())