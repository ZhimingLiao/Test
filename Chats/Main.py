#!/usr/bin/python3
# -*-encoding:utf-8-*-
__author__ = 'ANDY LIAO'
# 2018-11-18
import sys
import time
from PyQt5 import QtWidgets
from Chats import MyWindow
from wxpy import *


class Main(object):
    __TuLingKEY = '17ad9bebb636451db78be568c4ae40a0'
    bot = Bot(cache_path=False, console_qr=None, qr_path=None, qr_callback=None, login_callback=None,
                  logout_callback=None)
    __TuLing = Tuling(api_key=__TuLingKEY)

    def __init__(self, Name):
        super().__init__()
        self.Name = Name
        self.chats = MyWindow()

    def start(self):
        self.chats.show()
        sys.exit(app.exec_())

    @bot.register()
    def reply_my_friend(msg):
        time.sleep(5)
        Main.__TuLing.do_reply(msg)


if __name__ == '__main__':
    Main('1').start()
    # embed()


