#!/usr/bin/python3
# -*-encoding:utf-8-*-
__author__ = 'ANDY LIAO'
# 2018-11-18
import threading
import datetime
import time


class ThreadTimeChange(threading.Thread):
    def __init__(self, threadID, UserName):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.UserName = UserName

    def run(self):
        while True:
            self.UserName.setText('当前时间:'+datetime.datetime.now().strftime('%H:%M:%S'))
            time.sleep(1)
