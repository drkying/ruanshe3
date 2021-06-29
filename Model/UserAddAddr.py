from PyQt5 import QtCore, QtWidgets
from Model.Values import Values
from Model.dataUtils import *
from View import UserAddAddrWindow


class UserAddAddr(QtWidgets.QMainWindow, UserAddAddrWindow.Ui_MainWindow):
    switch_to_manage = QtCore.pyqtSignal()
    switch_to_subscribe = QtCore.pyqtSignal()
    pre_window = 0

    def __init__(self, pre):
        super(UserAddAddr, self).__init__()
        self.setupUi(self)
        self.initial(pre)

    def initial(self, pre):
        self.pushButton_add.clicked.connect(self.add_addr)
        self.pre_window = pre

    def add_addr(self):
        phone = str(self.lineEdit_phone.text())
        addr = str(self.lineEdit_addr.text())
        if not is_legal(phone) or not is_legal(addr):
            WarningBox(self, "手机号或地址存在非法字符，请重试")
            self.lineEdit_addr.clear()
            self.lineEdit_phone.clear()
            return
        connect, cursor = sqlconn()
        sql_test = "select * from address where usrname='" + Values.CurrentUser + "' and phone='" + phone + "' and addr='" + addr + "'"
        if cursor.execute(sql_test) > 0:
            WarningBox(self, "该地址已存在，请重试")
            self.lineEdit_addr.clear()
            self.lineEdit_phone.clear()
        else:
            sql = "Insert into address values ('" + Values.CurrentUser + "','" + phone + "','" + addr + "')"
            try:
                cursor.execute(sql)
            except Exception as e:
                connect.rollback()
                WarningBox(self, "sql新增地址失败，请重试")
                print(e)
            else:
                connect.commit()
                SuccBox(self, "新增地址成功")
                if self.pre_window == 1:
                    self.switch_to_manage.emit()
                elif self.pre_window == 2:
                    self.switch_to_subscribe.emit()

        connect.close()
