# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 广医五院  志明  2018-12-10 21:44
# 当前计算机登录名称 :广州医科大学附属第五医院
# 项目名称  :
# 编译器   :PyCharm
__author____ = '志明'
__time__ = '2018-12-10 21:44'


import pymssql
class MSSQL:
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        if not self.db:
            raise(NameError,"没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
        cur = self.conn.cursor()
        if not cur:
            raise(NameError,"连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecNonQuery(self,sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()

ms = MSSQL(host="192.168.1.1",user="sa",pwd="sa",db="testdb")
reslist = ms.ExecQuery("select * from webuser")
for i in reslist:
    print(i)

newsql="update webuser set name='%s' where id=1"%u'测试'
print(newsql)
ms.ExecNonQuery(newsql.encode('utf-8'))



if __name__ == '__main__':
    pass