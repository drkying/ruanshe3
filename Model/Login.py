import hashlib

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

from Model.Register import Register
from Model.Values import Values
from Model.dataUtils import sqlconn


class Login_Window(QtWidgets.QMainWindow):

    def __init__(self, gui, reg):
        super(Login_Window, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.gui = gui
        self.reg = reg

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386, 127)
        MainWindow.setWindowIcon(QIcon(''
                                       ''
                                       'logo.png'))
        MainWindow.setStyleSheet("background-image:url(logo.jpg)")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 24, 100, 24))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 54, 100, 24))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(200, 24, 48, 24))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(200, 54, 48, 24))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 90, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralWidget)

        self.pushButton.clicked.connect(self.word_get)
        # self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.register)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "报刊订阅系统"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "请输入帐号"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "请输入密码"))
        self.lineEdit_2.returnPressed.connect(self.word_get)
        self.label.setText(_translate("MainWindow", "帐 号"))
        self.label_2.setText(_translate("MainWindow", "密 码"))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.pushButton_2.setText(_translate("MainWindow", "注册"))

    def register(self):
        self.hide()
        self.reg.show()

    def word_get(self):
        connect, cursor = sqlconn()
        login_user = self.lineEdit.text()
        login_password = self.lineEdit_2.text()
        passwd = hashlib.md5(login_password.encode('UTF-8')).hexdigest()
        sql_root = "select * from root where usrname='" + login_user + "' and passwd='" + passwd + "'"
        sql_user = "select * from user where usrname='" + login_user + "' and passwd='" + passwd + "'"
        res_root = cursor.execute(sql_root)
        res_user = cursor.execute(sql_user)
        if res_root > 0:
            Values.IsRootLogin = True
            Values.CurrentUser = login_user
            self.gui.show()
            self.close()
        elif res_user > 0:
            Values.IsUserLogin = True
            Values.CurrentUser = login_user
            self.gui.show()
            self.close()
        else:
            QMessageBox.warning(self,
                                "警告",
                                "用户名或密码错误！",
                                QMessageBox.Yes)
            self.lineEdit.setFocus()
        self.gui.refreshAll()
        connect.close()
