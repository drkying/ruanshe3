import qdarkstyle
from PyQt5 import QtCore, QtWidgets
from Model.dataUtils import *
from View import UserAddAddrWindow


class UserAddAddr(QtWidgets.QMainWindow, UserAddAddrWindow.Ui_MainWindow):

    def __init__(self):
        super(UserAddAddr, self).__init__()
        self.setupUi(self)
        self.initial()
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def initial(self):
        self.pushButton_add.clicked.connect(self.add_addr)

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
                self.close()

        connect.close()
