# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserAddAddrWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 337)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 30, 131, 31))
        self.label.setObjectName("label")
        self.lineEdit_addr = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_addr.setGeometry(QtCore.QRect(130, 140, 171, 31))
        self.lineEdit_addr.setObjectName("lineEdit_addr")
        self.lineEdit_phone = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_phone.setGeometry(QtCore.QRect(130, 80, 171, 31))
        self.lineEdit_phone.setObjectName("lineEdit_phone")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(160, 200, 112, 32))
        self.pushButton_add.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/zengjia.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_add.setIcon(icon)
        self.pushButton_add.setObjectName("pushButton_add")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">新增地址</span></p></body></html>"))
        self.lineEdit_addr.setPlaceholderText(_translate("MainWindow", "在此输入地址信息"))
        self.lineEdit_phone.setPlaceholderText(_translate("MainWindow", "在此输入电话号码"))
        self.pushButton_add.setText(_translate("MainWindow", "新增地址"))
        self.pushButton_add.setShortcut(_translate("MainWindow", "Return"))
import resource_rc