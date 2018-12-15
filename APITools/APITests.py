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
import os
import datetime
from threading import Thread
import XMLFormat


class APITest(QtWidgets.QMainWindow, APITestUI.Ui_APITest):

    def __init__(self):
        super(APITest, self).__init__()
        self.setupUi(self)
        self.t = ThreadTimeChange.ThreadTimeChange('APITools', self.Timer)
        self.URL.setText('http://192.168.8.63:37777/EaiServer')
        self.OutPut.setPlainText('此处为出参')
        # self.Input.setPlainText('此处为入参')

    def closeEvent(self, *args, **kwargs):
        super().closeEvent(*args, **kwargs)
        self.reject()

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
            data = PostData.PostData(url, datas).getData().lstrip().rstrip().replace('\n', '')\
                .replace('\t', '').replace('\n\r', '')
            data = data.replace('<?xml version="1.0" encoding="GB2312"?>', '<?xml version="1.0" encoding="utf-8"?>')
            data = XMLFormat.XMLFormat.BsXML(data)
            self.OutPut.setPlainText(data)
            self.LookUp.setText('测试')
            Thread(target=self.LogWrite, args=(datas, data)).start()


    def LogWrite(self, StrInput, StrOutput):
        FileDir = r'日志文件'
        if os.path.isdir(FileDir) is False:
            os.mkdir(FileDir)
        FileName = os.path.join(FileDir, datetime.datetime.now().strftime('%Y-%m-%d') + r'.txt')
        StrInput = StrInput.replace('<?xml version="1.0" encoding="GB2312"?>', '')
        StrInput = XMLFormat.XMLFormat.BsXML(StrInput)

        with open(FileName, 'a+', encoding='utf-8') as fp:
            fp.writelines(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\t入参和出参日志:')
            fp.write('\n')
            fp.writelines('*' * 15 + '以下是入参' + '*' * 15)
            fp.write('\n')
            fp.writelines(StrInput)
            fp.write('\n')
            fp.writelines('*' * 15 + '以下是出参' + '*' * 15)
            fp.write('\n')
            fp.writelines(StrOutput)
            fp.write('\n\n')

    def showInfo(self, strdata):
        QtWidgets.QMessageBox.question(None, '温馨提示', strdata, QtWidgets.QMessageBox.Yes)

    def reject(self):
        self.t.stop()
        self.accept()

    def ClearData(self):
        self.OutPut.setPlainText('')
        self.Input.setPlainText('')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    APITools = APITest()
    APITools.t.start()
    APITools.show()

    # t.join()
    sys.exit(app.exec_())
