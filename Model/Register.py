import hashlib
import time

import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import qApp

from Model.dataUtils import *
from View import RegisterWindow


class Register(QtWidgets.QMainWindow, RegisterWindow.Ui_MainWindow):

    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)
        self.initial()
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def closeEvent(self, event):
        event.ignore()
        qApp.exit(1111)

    def initial(self):
        self.pushButton_register.clicked.connect(self.register)

    def clear_line_edit(self):
        self.lineEdit_addr.clear()
        self.lineEdit_name.clear()
        self.lineEdit_usrname.clear()
        self.lineEdit_passwd.clear()
        self.lineEdit_passwd_confirm.clear()
        self.lineEdit_phone.clear()

    def register(self):
        '''获取输入框内信息'''
        usrname = str(self.lineEdit_usrname.text())
        passwd = str(self.lineEdit_passwd.text())
        passwd = hashlib.md5(passwd.encode('UTF-8')).hexdigest()
        passwd_confirm = str(self.lineEdit_passwd_confirm.text())
        passwd_confirm = hashlib.md5(passwd_confirm.encode('UTF-8')).hexdigest()
        name = str(self.lineEdit_name.text())
        sex = str(self.comboBox_sex.currentText())
        dept = str(self.comboBox_dept.currentText())
        phone = str(self.lineEdit_phone.text())
        addr = str(self.lineEdit_addr.text())

        connect, cursor = sqlconn()
        sqltest = "Select * from user where usrname='" + usrname + "'"

        if usrname == "":
            WarningBox(self, "用户名不能为空，请重试")
        elif not is_legal(usrname):
            WarningBox(self, "用户名含有非法字符，注册失败")
            self.clear_line_edit()
        elif passwd != passwd_confirm:
            WarningBox(self, "两次密码不一致，请重试")
            self.clear_line_edit()
        elif not is_legal(name):
            WarningBox(self, "姓名含有非法字符，注册失败")
            self.clear_line_edit()
        elif not is_legal(phone) or not is_int_id(phone):
            WarningBox(self, "手机号非法，注册失败")
            self.clear_line_edit()
        elif not is_legal(addr):
            WarningBox(self, "地址含有非法字符，注册失败")
            self.clear_line_edit()
        else:
            if cursor.execute(sqltest) > 0:
                WarningBox(self, "该用户已存在，注册失败！")
                self.clear_line_edit()
            else:
                sql_user = "Insert into user values ('" + usrname + "','" + passwd + "','" + name + "','" + sex + "','" + dept + "')"
                sql_addr = "Insert into address values ('" + usrname + "','" + phone + "','" + addr + "')"
                try:
                    cursor.execute(sql_user)
                    cursor.execute(sql_addr)
                except Exception as e:
                    connect.rollback()
                    WarningBox(self, "注册失败")
                    print(e)
                else:
                    connect.commit()
                    QMessageBox.information(self,
                                            "恭喜",
                                            usrname + ",注册成功",
                                            QMessageBox.Yes)
                    qApp.exit(1111)

        connect.close()
