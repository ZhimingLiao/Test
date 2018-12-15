# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# 广医五院  志明  2018-12-11 8:24
# 当前计算机登录名称 :广州医科大学附属第五医院
# 项目名称  :
# 编译器   :PyCharm
__author____ = '志明'
__time__ = '2018-12-11 8:24'
__doc__ = '''使用pyodbc进行数据库连接并且进行简单的操作'''


import pyodbc


class MSSQLHelper:
    # 初始化数据
    def __init__(self, host='127.0.0.1', port=1433, user='sa', password='sql', db='master'):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.cursor = None
        self.conn = None

    # 获取连接对象
    def __GetConnection(self):
        if self.cursor:
            print('使用已经使用过的游标')
            return self.cursor
        else:
            try:
                ConnInfo = 'DRIVER={SQL Server};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s;'%(self.host, self.db, self.user, self.password)
                self.conn = pyodbc.connect(ConnInfo, unicode_results=True)
            except Exception:
                print('错误')
                pass
            else:
                self.cursor = self.conn.cursor()
                return self.cursor

    def __del__(self):
        if self.cursor:
            print('游标关闭!')
            self.cursor.close()
            self.cursor = None
        if self.conn:
            print('连接关闭!')
            self.conn.close()
            self.conn = None

    # 执行查询
    def exec_query(self, sql):
        try:
            cursor = self.__GetConnection()
            cursor.execute(sql)
        except Exception:
            return('配置出错!')
        else:
            DataList = cursor.fetchall()
            return DataList

    # 获取分页查询结果
    def query_page(self, sql, skipCnt, pageSize):
        try:
            cursor = self.__GetConnection()
        except:
            return '查询出错!'
        else:
            cursor.execute(sql)
            cursor.skip(skipCnt)
            return cursor.fetchmany(pageSize)

    # 执行sql增删修改,返回受影响的条数
    def exec_sql(self, sql):
        try:
            cursor = self.__GetConnection()
        except:
            print('语句有问题')
        else:
            count = cursor.execute(sql).rowcount
            self.conn.commit()
            return count


if __name__ == '__main__':
    conn_info = {'host': '172.16.230.100', 'user': 'sa', 'password': 'sql', 'db': 'hismz'}
    t = MSSQLHelper(**conn_info)
    sql = '''select * from temp_error where p_id = '{p_id}' '''.format(p_id='000000033300')
    sql2 = ''' update temp_error set pay_unit = 88 where p_id = '{p_id}' order by p_id asc '''.format(p_id='000000033300')
    sql3 = ''' select p_id , name from mz_patient order by p_id asc'''
    # print(t.ExecQuery(sql))
    # print(t.ExecSQL(sql2))
    # print(t.query_page(sql3, 5, 10)[:3:])
    print(t.exec_query("select count(*) from mz_patient")[0][0])
