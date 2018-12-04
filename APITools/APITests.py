#!/usr/bin/python3
# -*-encoding:utf-8-*-
__author__ = 'ANDY LIAO'
# 2018-11-24
import sys
import re

from PyQt5 import QtWidgets
import APITestUI
import ThreadTimeChange
import PostData


class APITest(QtWidgets.QMainWindow, APITestUI.Ui_APITest):

    def __init__(self):
        super(APITest, self).__init__()
        self.setupUi(self)
        self.t = ThreadTimeChange.ThreadTimeChange('APITools', self.Timer)

    def LookUpData(self):
        datas = self.Input.toPlainText().lstrip().rstrip().replace('\n', '').replace('\t', '').replace('\n\r', '')
        if datas == '':
            self.showInfo('入参不能为空!')
            return
        url = self.URL.toPlainText().lstrip().rstrip().replace('\n', '').replace('\t', '')\
            .replace('\n\r', '')
        if url == '' or (re.match('[a-zA-z]+://[^\s]*', url) is None):
            self.showInfo('URL不能为空或者URL地址不对!')
            return
        if datas != '' and url != '' and re.match('[a-zA-z]+://[^\s]*', url):
            self.LookUp.setText('已发送')
            data = PostData.PostData(url, datas).getData()
            self.OutPut.setPlainText(data)
            self.LookUp.setText('测试')

    def showInfo(self, strdata):
        QtWidgets.QMessageBox.question(None, '温馨提示', strdata, QtWidgets.QMessageBox.Yes)

    def reject(self):
        self.t.stop()
        self.accept()

    def BfXML(self, StrXML):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    APITools = APITest()
    APITools.t.start()
    APITools.show()
    # t.join()
    sys.exit(app.exec_())
