import qdarkstyle
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from Model.Values import Values
from Model.dataUtils import *
from View import UserSettleWindow


class UserSettle(QtWidgets.QMainWindow, UserSettleWindow.Ui_MainWindow):
    money = 0

    def __init__(self):
        super(UserSettle, self).__init__()
        self.setupUi(self)
        self.initial()
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def initial(self):
        self.pushButton_settle.clicked.connect(self.settle)
        self.pushButton_fresh.clicked.connect(self.show_subscribe)
        self.show_subscribe()

    def show_subscribe(self):
        connect, cursor = sqlconn()
        sql = "select user.name, subscription.phone, subscription.addr, newspaper.newsname, " \
              "newspaper.price, subscription.count, subscription.pay, subscription.unpay " \
              "from user inner join subscription " \
              "on (user.usrname=subscription.usrname) " \
              "inner join newspaper " \
              "on (subscription.newsid=newspaper.newsid) " \
              "where user.usrname='" + Values.CurrentUser + "'"
        row = cursor.execute(sql)
        self.tableWidget.setRowCount(row)
        results = cursor.fetchall()
        for i in range(row):
            for j in range(8):
                temp_data = results[i][j]
                data = QTableWidgetItem(str(temp_data))
                self.tableWidget.setItem(i, j, data)

        sql = "select sum(unpay) from subscription where usrname='" + Values.CurrentUser + "'"
        cursor.execute(sql)
        results = cursor.fetchall()
        self.money = results[0][0]
        pay = "<html><head/><body><p><span style=\" font-size:24pt;\">" + str(self.money) + "</span></p></body></html>"
        connect.close()

        self.label_money.setText(QtCore.QCoreApplication.translate("MainWindow", pay))

    def settle(self):
        connect, cursor = sqlconn()
        sql = "Update subscription set unpay=0 where usrname='" + Values.CurrentUser + "'"
        try:
            cursor.execute(sql)
        except Exception as e:
            connect.rollback()
            WarningBox(self, "sql更新失败")
            print(e)
        else:
            connect.commit()
            SuccBox(self, "成功结算金额" + str(self.money) + "，欢迎下次光临。")
            self.show_subscribe()

        connect.close()
