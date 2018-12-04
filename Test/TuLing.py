#!/usr/bin/python3
# -*-encoding:utf-8-*-
__author__ = 'ANDY LIAO'
# 2018-11-20
from wxpy import *


class TuLing:

    __TuLingKEY = '17ad9bebb636451db78be568c4ae40a0'
    __TuLing = None

    @classmethod
    def getTuLing(cls):
        if TuLing.__TuLing is None:
            TuLing.__TuLing = Tuling(api_key=TuLing.__TuLingKEY)
        return TuLing.__TuLing
