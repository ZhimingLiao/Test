# -*- coding:utf-8 -*-
__author__ = '广州医科大学附属第五医院/志明'
__time__ = '2018-11-18 10:26'

import sys
from PyQt5 import QtWidgets
from Chat import Ui_Chat


class Test(QtWidgets.QMainWindow, Ui_Chat):
    def __init__(self):
        super(Test, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    test = Test()
    test.show()
    sys.exit(app.exec_())

