#!/usr/bin/python3
# -*-encoding:utf-8-*-
__author__ = 'ANDY LIAO'
# 2018-11-19
import time
from threading import Thread


def countdown(n):
    while n > 0:
        with open('thread_log.log', 'a') as f:
            f.write('T-minus'+str(n))
        n -= 1
        time.sleep(5)


t = Thread(target=countdown, args=(5, ), daemon=True)
t.start()
# t.join()
time.sleep(20)

if t.is_alive():
    print('running')
else:
    print('completed')

