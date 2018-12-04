#!/usr/bin/python3
# -*-encoding:utf-8-*-
__author__ = 'ANDY LIAO'
# 2018-11-18

import time
from threading import Thread
from wxpy import *


class WXRobt:
    __TuLingKEY = '17ad9bebb636451db78be568c4ae40a0'
    __TuLing = None
    __Bot = None

    @classmethod
    def getBot(cls):
        if WXRobt.__Bot is None:
            WXRobt.__Bot = Bot(cache_path=True, console_qr=None, qr_path=None, qr_callback=None, login_callback=None, logout_callback=None)
        return WXRobt.__Bot

    @classmethod
    def getTuLing(cls):
        if WXRobt.__TuLing is None:
            WXRobt.__TuLing = Tuling(api_key=WXRobt.__TuLingKEY)
        return WXRobt.__TuLing
