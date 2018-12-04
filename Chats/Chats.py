from PyQt5 import QtWidgets
import UiChat
from ThreadTimeChange import ThreadTimeChange
import datetime
from PyQt5.QtCore import QStringListModel
from wxrobt import WXRobt

class MyWindow(QtWidgets.QMainWindow, UiChat.Ui_Chat):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.UserName.setText('欢迎使用')
        self.Time.setText(datetime.datetime.now().strftime('%H:%M:%S'))
        ThreadTimeChange('Chats', self.Time).start()


if __name__ == '__main__':
    import sys
    bot = WXRobt.getBot()
    app = QtWidgets.QApplication(sys.argv)
    mywindow = MyWindow()
    ls = ['aa', 'bb']
    slm = QStringListModel()
    slm.setStringList(ls)
    mywindow.listView.setModel(slm)
    mywindow.show()
    t = ThreadTimeChange(1, mywindow.Time)
    t.start()
    # t.join()

    @bot.register()
    def reply_my_friend(msg):
        print(msg)
        # time.sleep(5)
        # print(TuLing.do_reply(msg))
        # print(TuLing.TuLing.getTuLing().do_reply(msg))
        #     print(TuLing.TuLing.getTuLing().do_reply(msg))
        ls.append(WXRobt.getTuLing().do_reply(msg))
        slm.setStringList(ls)
        mywindow.listView.setModel(slm)
    sys.exit(app.exec_())
    # t.join()


