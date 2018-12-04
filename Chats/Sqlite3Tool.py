#!/usr/bin/python3
# -*-encoding:utf-8-*-
__author__ = 'ANDY LIAO'
# 2018-11-20

# python sqlite

# Author : Hongten
# MailTo : hongtenzone@foxmail.com
# QQ     : 648719819
# Blog   : http://www.cnblogs.com/hongten
# Create : 2013-08-09
# Version: 1.0

# DB-API 2.0 interface for SQLite databases

import sqlite3
import os

'''SQLite数据库是一款非常小巧的嵌入式开源数据库软件，也就是说
没有独立的维护进程，所有的维护都来自于程序本身。
在python中，使用sqlite3创建数据库的连接，当我们指定的数据库文件不存在的时候
连接对象会自动创建数据库文件；如果数据库文件已经存在，则连接对象不会再创建
数据库文件，而是直接打开该数据库文件。
    连接对象可以是硬盘上面的数据库文件，也可以是建立在内存中的，在内存中的数据库
    执行完任何操作后，都不需要提交事务的(commit)

    创建在硬盘上面： conn = sqlite3.connect('c:\\test\\test.db')
    创建在内存上面： conn = sqlite3.connect('"memory:')

    下面我们一硬盘上面创建数据库文件为例来具体说明：
    conn = sqlite3.connect('c:\\test\\hongten.db')
    其中conn对象是数据库链接对象，而对于数据库链接对象来说，具有以下操作：

        commit()            --事务提交
        rollback()          --事务回滚
        close()             --关闭一个数据库链接
        cursor()            --创建一个游标

    cu = conn.cursor()
    这样我们就创建了一个游标对象：cu
    在sqlite3中，所有sql语句的执行都要在游标对象的参与下完成
    对于游标对象cu，具有以下具体操作：

        execute()           --执行一条sql语句
        executemany()       --执行多条sql语句
        close()             --游标关闭
        fetchone()          --从结果中取出一条记录
        fetchmany()         --从结果中取出多条记录
        fetchall()          --从结果中取出所有记录
        scroll()            --游标滚动

'''

class Sqlite3Tool:
    # global var
    # 数据库文件绝句路径
    DB_FILE_PATH = ''
    # 表名称
    TABLE_NAME = ''
    # 是否打印sql
    SHOW_SQL = True

    def get_conn(self, path):
        '''获取到数据库的连接对象，参数为数据库文件的绝对路径
        如果传递的参数是存在，并且是文件，那么就返回硬盘上面改
        路径下的数据库文件的连接对象；否则，返回内存中的数据接
        连接对象'''
        if os.path.exists(path) and os.path.isfile(path):
            print('硬盘上面:[{}]'.format(path))
            return sqlite3.connect(path)
        else:
            print('内存上面:[:memory:]')
            return sqlite3.connect(':memory:')

    def get_cursor(self, conn):
        '''该方法是获取数据库的游标对象，参数为数据库的连接对象
        如果数据库的连接对象不为None，则返回数据库连接对象所创
        建的游标对象；否则返回一个游标对象，该对象是内存中数据
        库连接对象所创建的游标对象'''
        if conn is not None:
            return conn.cursor()
        else:
            return self.get_conn('').cursor()

    def drop_table(self, conn, table):
        '''如果表存在,则删除表，如果表中存在数据的时候，使用该
        方法的时候要慎用！'''
        sql = 'DROP TABLE IF EXISTS ' + table
        if table is not None and table != '':
            if SHOW_SQL:
                print('执行sql:[{}]'.format(sql))
            cu = self.get_cursor(conn)
            cu.execute(sql)
            conn.commit()
            print('删除数据库表[{}]成功!'.format(table))
            self.close_all(conn, cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def create_table(self, conn, sql):
        '''创建数据库表：student'''
        if sql is not None and sql != '':
            cu = self.get_cursor(conn)
            if SHOW_SQL:
                print('执行sql:[{}]'.format(sql))
            cu.execute(sql)
            conn.commit()
            print('创建数据库表[student]成功!')
            self.close_all(conn, cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def close_all(self, conn, cu):
        '''关闭数据库游标对象和数据库连接对象'''
        try:
            if cu is not None:
                cu.close()
        finally:
            if cu is not None:
                cu.close()

    def save(self, conn, sql, data):
        '''插入数据'''
        if sql is not None and sql != '':
            if data is not None:
                cu = self.get_cursor(conn)
                for d in data:
                    if SHOW_SQL:
                        print('执行sql:[{}],参数:[{}]'.format(sql, d))
                    cu.execute(sql, d)
                    conn.commit()
                self.close_all(conn, cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def fetchall(self, conn, sql):
        '''查询所有数据'''
        if sql is not None and sql != '':
            cu = self.get_cursor(conn)
            if SHOW_SQL:
                print('执行sql:[{}]'.format(sql))
            cu.execute(sql)
            r = cu.fetchall()
            if len(r) > 0:
                for e in range(len(r)):
                    print(r[e])
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def fetchone(self, conn, sql, data):
        '''查询一条数据'''
        if sql is not None and sql != '':
            if data is not None:
                # Do this instead
                d = (data,)
                cu = self.get_cursor(conn)
                if SHOW_SQL:
                    print('执行sql:[{}],参数:[{}]'.format(sql, data))
                cu.execute(sql, d)
                r = cu.fetchall()
                if len(r) > 0:
                    for e in range(len(r)):
                        print(r[e])
            else:
                print('the [{}] equal None!'.format(data))
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def update(self, conn, sql, data):
        '''更新数据'''
        if sql is not None and sql != '':
            if data is not None:
                cu = self.get_cursor(conn)
                for d in data:
                    if SHOW_SQL:
                        print('执行sql:[{}],参数:[{}]'.format(sql, d))
                    cu.execute(sql, d)
                    conn.commit()
                self.close_all(conn, cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def delete(self, conn, sql, data):
        '''删除数据'''
        if sql is not None and sql != '':
            if data is not None:
                cu = self.get_cursor(conn)
                for d in data:
                    if SHOW_SQL:
                        print('执行sql:[{}],参数:[{}]'.format(sql, d))
                    cu.execute(sql, d)
                    conn.commit()
                self.close_all(conn, cu)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def __init__(self):
        # 数据库文件绝句路径
        global DB_FILE_PATH
        DB_FILE_PATH = 'c:\\test\\hongten.db'
        # 数据库表名称
        global TABLE_NAME
        TABLE_NAME = 'student'
        # 是否打印sql
        global SHOW_SQL
        SHOW_SQL = True
        print('show_sql : {}'.format(SHOW_SQL))

    def execute(self, sql, args=[], result_dict=True, commit=True) -> list:
        """
        执行数据库操作的通用方法
        Args:
        sql: sql语句
        args: sql参数
        result_dict: 操作结果是否用dict格式返回
        commit: 是否提交事务
        Returns:
        list 列表，例如：
        [{'id': 1, 'name': '张三'}, {'id': 2, 'name': '李四'}]
        """
        if result_dict:
            self.get_conn().row_factory = self._dict_factory
        else:
            self.get_conn().row_factory = None
        # 获取游标
        _cursor = self.get_conn().cursor()
        # 执行SQL获取结果
        _cursor.execute(sql, args)
        if commit:
            self.get_conn().commit()
        data = _cursor.fetchall()
        _cursor.close()
        return data
