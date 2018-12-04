# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Chat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Chat(object):
    def setupUi(self, Chat):
        Chat.setObjectName("Chat")
        Chat.setWindowModality(QtCore.Qt.WindowModal)
        Chat.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Chat.sizePolicy().hasHeightForWidth())
        Chat.setSizePolicy(sizePolicy)
        Chat.setMinimumSize(QtCore.QSize(800, 600))
        Chat.setMaximumSize(QtCore.QSize(800, 600))
        Chat.setBaseSize(QtCore.QSize(300, 500))
        font = QtGui.QFont()
        font.setFamily("冬青黑体简体中文 W3")
        Chat.setFont(font)
        Chat.setMouseTracking(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("chat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Chat.setWindowIcon(icon)
        Chat.setToolTip("")
        Chat.setToolTipDuration(1)
        Chat.setAutoFillBackground(False)
        Chat.setStyleSheet("background-color: rgb(75, 75, 75);")
        self.label = QtWidgets.QLabel(Chat)
        self.label.setGeometry(QtCore.QRect(40, 220, 71, 31))
        font = QtGui.QFont()
        font.setFamily("冬青黑体简体中文 W3")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(Chat)
        self.graphicsView.setGeometry(QtCore.QRect(5, 260, 150, 150))
        self.graphicsView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.graphicsView.setStyleSheet("border-color: rgb(255, 0, 127);")
        self.graphicsView.setObjectName("graphicsView")
        self.UserName = QtWidgets.QLabel(Chat)
        self.UserName.setGeometry(QtCore.QRect(30, 30, 100, 20))
        font = QtGui.QFont()
        font.setFamily("冬青黑体简体中文 W3")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.UserName.setFont(font)
        self.UserName.setStyleSheet("color: rgb(255, 255, 255);")
        self.UserName.setTextFormat(QtCore.Qt.RichText)
        self.UserName.setAlignment(QtCore.Qt.AlignCenter)
        self.UserName.setObjectName("UserName")
        self.listView = QtWidgets.QListView(Chat)
        self.listView.setGeometry(QtCore.QRect(160, 0, 640, 600))
        self.listView.setStyleSheet("background-color: rgb(148, 222, 222);")
        self.listView.setObjectName("listView")
        self.Time = QtWidgets.QLabel(Chat)
        self.Time.setGeometry(QtCore.QRect(5, 560, 150, 30))
        font = QtGui.QFont()
        font.setFamily("冬青黑体简体中文 W3")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Time.setFont(font)
        self.Time.setStyleSheet("color: rgb(255, 255, 255);")
        self.Time.setTextFormat(QtCore.Qt.RichText)
        self.Time.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Time.setObjectName("Time")

        self.retranslateUi(Chat)
        QtCore.QMetaObject.connectSlotsByName(Chat)

    def retranslateUi(self, Chat):
        _translate = QtCore.QCoreApplication.translate
        Chat.setWindowTitle(_translate("Chat", "自动聊天工具"))
        self.label.setText(_translate("Chat", "扫码确认"))
        self.UserName.setText(_translate("Chat", "用户名"))
        self.Time.setText(_translate("Chat", "时间:"))

