# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'APITest.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_APITest(object):
    def setupUi(self, APITest):
        APITest.setObjectName("APITest")
        APITest.resize(1000, 700)
        APITest.setMaximumSize(QtCore.QSize(1000, 700))
        font = QtGui.QFont()
        font.setPointSize(10)
        APITest.setFont(font)
        APITest.setStyleSheet("background-color: rgb(199, 237, 204);")
        self.Timer = QtWidgets.QLabel(APITest)
        self.Timer.setGeometry(QtCore.QRect(710, 640, 201, 30))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Timer.setFont(font)
        self.Timer.setObjectName("Timer")
        self.Timer_3 = QtWidgets.QLabel(APITest)
        self.Timer_3.setGeometry(QtCore.QRect(230, 70, 201, 31))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Timer_3.setFont(font)
        self.Timer_3.setObjectName("Timer_3")
        self.Timer_4 = QtWidgets.QLabel(APITest)
        self.Timer_4.setGeometry(QtCore.QRect(730, 70, 201, 31))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Timer_4.setFont(font)
        self.Timer_4.setObjectName("Timer_4")
        self.INFO = QtWidgets.QLabel(APITest)
        self.INFO.setGeometry(QtCore.QRect(30, 620, 291, 20))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.INFO.setFont(font)
        self.INFO.setStyleSheet("color: rgb(118, 118, 118);")
        self.INFO.setObjectName("INFO")
        self.label = QtWidgets.QLabel(APITest)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(30, 500, 351, 61))
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setPixmap(QtGui.QPixmap("D:/PycharmProjects/Test/APITools/hq-logo.png"))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(APITest)
        self.layoutWidget.setGeometry(QtCore.QRect(710, 590, 263, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(18)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LookUp = QtWidgets.QPushButton(self.layoutWidget)
        self.LookUp.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(18)
        self.LookUp.setFont(font)
        self.LookUp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LookUp.setStyleSheet("background-color: rgb(0, 255, 127);")
        self.LookUp.setObjectName("LookUp")
        self.horizontalLayout.addWidget(self.LookUp)
        self.Clear = QtWidgets.QPushButton(self.layoutWidget)
        self.Clear.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Clear.setFont(font)
        self.Clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Clear.setStyleSheet("background-color: rgb(181, 181, 181);")
        self.Clear.setObjectName("Clear")
        self.horizontalLayout.addWidget(self.Clear)
        self.Quit = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Quit.setFont(font)
        self.Quit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Quit.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Quit.setObjectName("Quit")
        self.horizontalLayout.addWidget(self.Quit)
        self.layoutWidget1 = QtWidgets.QWidget(APITest)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 30, 951, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Timer_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Timer_2.setFont(font)
        self.Timer_2.setObjectName("Timer_2")
        self.horizontalLayout_2.addWidget(self.Timer_2)
        self.URL = QtWidgets.QTextEdit(self.layoutWidget1)
        self.URL.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.URL.setFont(font)
        self.URL.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.URL.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.URL.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.URL.setLineWidth(0)
        self.URL.setMidLineWidth(1)
        self.URL.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.URL.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.URL.setLineWrapColumnOrWidth(1)
        self.URL.setObjectName("URL")
        self.horizontalLayout_2.addWidget(self.URL)
        self.layoutWidget2 = QtWidgets.QWidget(APITest)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 110, 951, 441))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Input = QtWidgets.QPlainTextEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Input.setFont(font)
        self.Input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Input.setPlainText("")
        self.Input.setObjectName("Input")
        self.horizontalLayout_3.addWidget(self.Input)
        self.OutPut = QtWidgets.QPlainTextEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.OutPut.setFont(font)
        self.OutPut.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OutPut.setReadOnly(True)
        self.OutPut.setPlainText("")
        self.OutPut.setObjectName("OutPut")
        self.horizontalLayout_3.addWidget(self.OutPut)
        self.INFO_2 = QtWidgets.QLabel(APITest)
        self.INFO_2.setGeometry(QtCore.QRect(30, 579, 351, 41))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.INFO_2.setFont(font)
        self.INFO_2.setStyleSheet("color: rgb(118, 118, 118);")
        self.INFO_2.setObjectName("INFO_2")
        self.INFO_3 = QtWidgets.QLabel(APITest)
        self.INFO_3.setGeometry(QtCore.QRect(30, 650, 451, 21))
        font = QtGui.QFont()
        font.setFamily("华文细黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.INFO_3.setFont(font)
        self.INFO_3.setObjectName("INFO_3")

        self.retranslateUi(APITest)
        self.Quit.clicked.connect(APITest.reject)
        self.LookUp.clicked.connect(self.LookUpData)
        self.Clear.clicked.connect(self.ClearData)
        QtCore.QMetaObject.connectSlotsByName(APITest)

    def retranslateUi(self, APITest):
        _translate = QtCore.QCoreApplication.translate
        APITest.setWindowTitle(_translate("APITest", "第三方接口调试工具"))
        self.Timer.setText(_translate("APITest", "当前时间:"))
        self.Timer_3.setText(_translate("APITest", "入参"))
        self.Timer_4.setText(_translate("APITest", "出参"))
        self.INFO.setText(_translate("APITest", "当前版本:V1.1    开发者: 志明"))
        self.LookUp.setToolTip(_translate("APITest", "点击进行测试"))
        self.LookUp.setText(_translate("APITest", "调用"))
        self.Clear.setToolTip(_translate("APITest", "点击进行清除"))
        self.Clear.setText(_translate("APITest", "重置"))
        self.Quit.setToolTip(_translate("APITest", "点击进行退出"))
        self.Quit.setText(_translate("APITest", "退出"))
        self.Timer_2.setText(_translate("APITest", "URL地址:"))
        self.URL.setToolTip(_translate("APITest", "此处输入你的URL地址"))
        self.URL.setPlaceholderText(_translate("APITest", "此处粘贴需要进行测试的URL地址(例如:http://172.16.230.100:37777/EaiServer)"))
        self.Input.setPlaceholderText(_translate("APITest", "此处为入参数据"))
        self.OutPut.setPlaceholderText(_translate("APITest", "此处为出参数据"))
        self.INFO_2.setText(_translate("APITest", "广州惠侨计算机科技有限公司"))
        self.INFO_3.setText(_translate("APITest", "说明:1.当前路径下会生成调用日志文件夹 2.适用于POST方式请求数据"))

