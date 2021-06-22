import hashlib

import pymysql
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QHeaderView, QGridLayout

from View import LoginWindow

class Values:
    CurrentUser = ""
    CurrentPermission = ""

    def clear(self):
        self.CurrentUser = ""
        self.CurrentPermission = ""


def sqlconn():
    connect = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="hityys123",
        database="Subscribe",
        autocommit=True
    )
    cursor = connect.cursor()
    return connect, cursor

def WarningBox(c, info):
    c.box = QMessageBox(QMessageBox.Warning, "Failed", info)
    yes = c.box.addButton('确定', QMessageBox.YesRole)
    c.box.setIcon(2)
    c.box.show()


def SuccBox(c, info):
    c.box = QMessageBox(QMessageBox.Information, "Success", info)
    yes = c.box.addButton('ok', QMessageBox.YesRole)
    c.box.setIcon(1)
    c.box.show()

class Login(QtWidgets.QMainWindow, LoginWindow.Ui_MainWindow):
    #switch_register = QtCore.pyqtSignal()
    #switch_login = QtCore.pyqtSignal()

    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.initial()

    def initial(self):
        self.pushButton_reset.clicked.connect(self.lineEdit_usrname.clear)
        self.pushButton_reset.clicked.connect(self.lineEdit_passwd.clear)
        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_register.clicked.connect(self.register)

    def register(self):
        self.switch_register.emit()

    def login(self):
        connect, cursor = sqlconn()
        '''获取输入框内信息'''
        usrname = str(self.lineEdit_usrname.text())
        passwd = str(self.lineEdit_passwd.text())
        passwd = hashlib.md5(passwd.encode('UTF-8')).hexdigest()
        permission = str(self.comboBox_Permissions.currentText())
        if True:
            if permission == "管理员":
                sql = "select * from root where usrname='" + usrname + "' and passwd='" + passwd + "'"
                Values.CurrentPermission = "root"
            else:
                sql = "select * from user where usrname='" + usrname + "' and passwd='" + passwd + "'"
                Values.CurrentPermission = "user"

            if cursor.execute(sql) > 0:
                SuccBox(self, usrname + '，登陆成功')
                Values.CurrentUser = usrname
                self.switch_login.emit()
            else:
                WarningBox(self, "登陆失败")
                self.lineEdit_passwd.clear()
                Values.CurrentUser = ""
                Values.CurrentPermission = ""
        else:
            Warning(self, "用户名输入非法字符，请重试")
            self.lineEdit_passwd.clear()
            self.lineEdit_usrname.clear()
        connect.close()