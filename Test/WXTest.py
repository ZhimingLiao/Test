#!/usr/bin/python3
# -*-encoding:utf-8-*-
__author__ = 'ANDY LIAO'
# 2018-11-20

import time
from wxpy import *
# import TuLing
from Chats.wxrobt import WXRobt

class WXTest:
    __bot = Bot(cache_path=True, console_qr=None, qr_path=None, qr_callback=None, login_callback=None,
              logout_callback=None)
    __TuLingKEY = '17ad9bebb636451db78be568c4ae40a0'
    # __TuLing = Tuling(api_key=__TuLingKEY)

    def __init__(self):
        if WXTest.__bot is None:
            WXTest.__bot = Bot(cache_path=True, console_qr=None, qr_path=None, qr_callback=None, login_callback=None,
                      logout_callback=None)
        if WXTest.__TuLing is None:
            Tuling(api_key=__TuLingKEY)


    def getBot(self):
        return WXTest.__bot

    def getTuLing(self):
        return WXTest.__TuLing


if __name__ == '__main__':
    # bot = WXTest().getBot()

    bot = WXRobt.getBot()
    # TuLingKEY = '17ad9bebb636451db78be568c4ae40a0'
    # TuLing = Tuling(api_key=TuLingKEY)
    # Tu = TuLing.TuLing.getTuLing()

    @bot.register()
    def reply_my_friend(msg):
        print(msg)
        # time.sleep(5)
        # print(TuLing.do_reply(msg))
        # print(TuLing.TuLing.getTuLing().do_reply(msg))
    #     print(TuLing.TuLing.getTuLing().do_reply(msg))
        print(WXRobt.getTuLing().do_reply(msg))
    bot.join()


