# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserAddrWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 465)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 0, 131, 41))
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 60, 241, 311))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(420, 220, 112, 32))
        self.pushButton_delete.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/shanchu.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_delete.setIcon(icon)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_update.setGeometry(QtCore.QRect(420, 180, 112, 32))
        self.pushButton_update.setFocusPolicy(QtCore.Qt.WheelFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/insert.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_update.setIcon(icon1)
        self.pushButton_update.setObjectName("pushButton_update")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 110, 291, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(420, 260, 112, 32))
        self.pushButton_add.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/zengjia.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_add.setIcon(icon2)
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_refresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_refresh.setGeometry(QtCore.QRect(420, 300, 112, 32))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/fresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_refresh.setIcon(icon3)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 635, 22))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt;\">地址管理</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "手机号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "地址"))
        self.pushButton_delete.setText(_translate("MainWindow", "删除"))
        self.pushButton_update.setText(_translate("MainWindow", "修改"))
        self.pushButton_update.setShortcut(_translate("MainWindow", "Return"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "在表格中选中需要修改的项后，在此输入修改后的值"))
        self.pushButton_add.setText(_translate("MainWindow", "新增地址"))
        self.pushButton_refresh.setText(_translate("MainWindow", "刷新"))
import resource_rc
