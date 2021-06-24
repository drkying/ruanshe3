# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BackupRecoverWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(696, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(400, 430, 112, 32))
        self.pushButton_back.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/back.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.pushButton_back.setIcon(icon)
        self.pushButton_back.setObjectName("pushButton_back")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 50, 451, 301))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.pushButton_backup = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_backup.setGeometry(QtCore.QRect(400, 380, 112, 32))
        self.pushButton_backup.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/beifen.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_backup.setIcon(icon1)
        self.pushButton_backup.setObjectName("pushButton_backup")
        self.pushButton_recover = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_recover.setGeometry(QtCore.QRect(540, 380, 112, 32))
        self.pushButton_recover.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/huifubeifen.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_recover.setIcon(icon2)
        self.pushButton_recover.setObjectName("pushButton_recover")
        self.pushButton_logout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_logout.setGeometry(QtCore.QRect(540, 430, 112, 32))
        self.pushButton_logout.setFocusPolicy(QtCore.Qt.StrongFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/log-out.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.pushButton_logout.setIcon(icon3)
        self.pushButton_logout.setObjectName("pushButton_logout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 696, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Backup & Recover"))
        self.pushButton_back.setText(_translate("MainWindow", "back"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "备份文件名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "备份时间"))
        self.pushButton_backup.setText(_translate("MainWindow", "备份"))
        self.pushButton_backup.setShortcut(_translate("MainWindow", "Return"))
        self.pushButton_recover.setText(_translate("MainWindow", "恢复备份"))
        self.pushButton_logout.setText(_translate("MainWindow", "Logout"))


import resource_rc
