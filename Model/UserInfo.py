import hashlib

from PyQt5 import QtCore, QtWidgets

from Model.dataUtils import *
from Model.Values import Values
from View import UserInfoWindow


class UserInfo(QtWidgets.QMainWindow, UserInfoWindow.Ui_MainWindow):
    switch_logout = QtCore.pyqtSignal()

    def __init__(self):
        super(UserInfo, self).__init__()
        self.setupUi(self)
        self.initial()

    def initial(self):
        self.showinfo()
        self.pushButton_changeinfo.clicked.connect(self.change_info)
        self.pushButton_changepasswd.clicked.connect(self.change_passwd)

    def showinfo(self):
        html_name = "<html><head/><body><p><span style=\" font-size:18pt;\">" + \
                    Values.CurrentUser + \
                    "</span></p></body></html>"
        self.label_usrname.setText(QtCore.QCoreApplication.translate("MainWindow", html_name))

        connect, cursor = sqlconn()
        sql = "select name, sex, dept from user where usrname='" + Values.CurrentUser + "'"
        cursor.execute(sql)
        results = cursor.fetchall()
        name = results[0][0]
        sex = results[0][1]
        dept = results[0][2]
        self.lineEdit_name.setText(name)
        self.comboBox_sex.setCurrentText(sex)
        self.comboBox_dept.setCurrentText(dept)
        connect.close()

    def change_info(self):
        name = str(self.lineEdit_name.text())
        sex = str(self.comboBox_sex.currentText())
        dept = str(self.comboBox_dept.currentText())
        if is_legal(name) == True :
            connect, cursor = sqlconn()
            sql = "Update user set name='" + name + "', sex='" + sex + "', dept='" + dept + "' where usrname='" + Values.CurrentUser + "'"
            try:
                cursor.execute(sql)
            except Exception as e:
                connect.rollback()
                WarningBox(self, "sql修改信息失败，请重试")
                print(e)
            else:
                connect.commit()
                SuccBox(self, "修改成功")
            connect.close()
        else:
            WarningBox(self, "信息不允许为空或存在非法字符，请重试")

        self.show()

    def clear_passwd_line(self):
        self.lineEdit_oldpasswd.clear()
        self.lineEdit_newpasswd.clear()
        self.lineEdit_confirm.clear()

    def logout(self):
        Values.CurrentUser = ""
        Values.CurrentPermission = ""
        self.switch_logout.emit()

    def change_passwd(self):
        oldpasswd = str(self.lineEdit_oldpasswd.text())
        oldpasswd = hashlib.md5(oldpasswd.encode('UTF-8')).hexdigest()
        newpasswd = str(self.lineEdit_newpasswd.text())
        confirm = str(self.lineEdit_confirm.text())

        connect, cursor = sqlconn()
        sql_test = "select * from user where usrname='" + Values.CurrentUser + "' and passwd='" + oldpasswd + "'"
        if cursor.execute(sql_test) > 0:
            if newpasswd == confirm:
                newpasswd = hashlib.md5(newpasswd.encode('UTF-8')).hexdigest()
                sql = "Update user set passwd='" + newpasswd + "' where usrname='" + Values.CurrentUser + "'"
                try:
                    cursor.execute(sql)
                except Exception as e:
                    connect.rollback()
                    WarningBox(self, "sql密码修改失败")
                    print(e)
                    self.clear_passwd_line()
                else:
                    connect.commit()
                    SuccBox(self, "密码修改成功请重新登陆")
                    self.logout()
            else:
                WarningBox(self, "新密码两次不一致，请重试！")
                self.clear_passwd_line()

        else:
            WarningBox(self, "旧密码错误，请重试！")
            self.clear_passwd_line()

        connect.close()
