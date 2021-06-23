from PyQt5 import QtCore, QtGui, QtWidgets

from Model.Values import Values
from Model.dataUtils import *
from View import MenuWindow


class Menu(QtWidgets.QMainWindow, MenuWindow.Ui_MainWindow):
    switch_logout = QtCore.pyqtSignal()

    switch_user_info = QtCore.pyqtSignal()
    switch_user_subscribe = QtCore.pyqtSignal()
    switch_user_manage = QtCore.pyqtSignal()
    switch_user_settle = QtCore.pyqtSignal()
    switch_user_addr = QtCore.pyqtSignal()

    switch_root_search = QtCore.pyqtSignal()
    switch_root_insert = QtCore.pyqtSignal()
    switch_root_statistics = QtCore.pyqtSignal()
    switch_root_backup = QtCore.pyqtSignal()

    def __init__(self):
        super(Menu, self).__init__()
        self.setupUi(self)
        self.initial()

    def initial(self):
        self.pushButton_logout.clicked.connect(self.logout)
        self.pushButton_next.clicked.connect(self.next)
        self.pushButton_userinfo.clicked.connect(self.userinfo)
        welcome = "Hi, " + Values.CurrentUser + "!"
        welcome_str = "<html><head/><body><p><span style=\" font-size:20pt;\">" + \
                      welcome + \
                      "</span></p></body></html>"
        self.label_welcome.setText(QtCore.QCoreApplication.translate("MainWindow", welcome_str))

        if Values.CurrentPermission == "user":
            self.comboBox_root.setVisible(False)
            self.comboBox_user.setVisible(True)
            self.pushButton_userinfo.setVisible(True)
        if Values.CurrentPermission == "root":
            self.comboBox_user.setVisible(False)
            self.comboBox_root.setVisible(True)
            self.pushButton_userinfo.setVisible(False)

    def logout(self):
        Values.CurrentUser = ""
        Values.CurrentPermission = ""
        self.switch_logout.emit()

    def userinfo(self):
        self.switch_user_info.emit()

    def next(self):
        if Values.CurrentPermission == "root":
            func = str(self.comboBox_root.currentText())
            if func == "订阅查询":
                self.switch_root_search.emit()
            if func == "报刊管理":
                self.switch_root_insert.emit()
            if func == "订阅统计":
                self.switch_root_statistics.emit()
            if func == "系统维护":
                self.switch_root_backup.emit()

        if Values.CurrentPermission == "user":
            func = str(self.comboBox_user.currentText())
            if func == "订阅报刊":
                self.switch_user_subscribe.emit()
            if func == "订阅管理":
                self.switch_user_manage.emit()
            if func == "金额结算":
                self.switch_user_settle.emit()
            if func == "地址管理":
                self.switch_user_addr.emit()
