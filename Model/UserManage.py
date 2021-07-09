import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from Model.dataUtils import *
from Model.Values import Values
from View import UserManagerWindow


class UserManager(QtWidgets.QMainWindow, UserManagerWindow.Ui_MainWindow):
    switch_back = QtCore.pyqtSignal()
    switch_logout = QtCore.pyqtSignal()
    news_id = ""
    time = ""

    def __init__(self):
        super(UserManager, self).__init__()
        self.setupUi(self)
        self.initial()

    def initial(self):
        self.pushButton_change.clicked.connect(self.change)
        self.pushButton_fresh.clicked.connect(self.show_subscribe)
        self.show_subscribe()
        self.tableWidget.itemClicked.connect(self.set_news_id)

    def set_news_id(self):
        select = self.tableWidget.selectedItems()
        if select:
            row = self.tableWidget.row(select[0])
            self.news_id = str(self.tableWidget.item(row, 3).text())
            self.time = str(self.tableWidget.item(row, 9).text())
            news_id_html = "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">" + "newsid: " + self.news_id + "</span></p></body></html>"
            self.label_newsid.setText(QtCore.QCoreApplication.translate("MainWindow", news_id_html))

    def show_subscribe(self):
        connect, cursor = sqlconn()
        sql = "select user.name, subscription.phone, subscription.addr, newspaper.newsid, " \
              "newspaper.newsname, newspaper.price, subscription.count, subscription.pay, subscription.unpay, subscription.time " \
              "from user inner join subscription " \
              "on (user.usrname=subscription.usrname) " \
              "inner join newspaper " \
              "on (subscription.newsid=newspaper.newsid) " \
              "where user.usrname='" + Values.CurrentUser + "'"
        row = cursor.execute(sql)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnWidth(9, 180)
        results = cursor.fetchall()
        for i in range(row):
            for j in range(10):
                temp_data = results[i][j]
                data = QTableWidgetItem(str(temp_data))
                self.tableWidget.setItem(i, j, data)
        connect.close()

    def change(self):
        if self.news_id == "":
            WarningBox(self, "请先在表中选中需要修改的记录")
            return
        count = self.spinBox_count.value()
        connect, cursor = sqlconn()
        sql_test = "select count, unpay from subscription where usrname='" + Values.CurrentUser + "' and newsid=" + self.news_id + " and time='" + self.time + "'"
        cursor.execute(sql_test)
        results = cursor.fetchall()
        usedcount = results[0][0]
        usedunpay = results[0][1]

        if count == 0:
            sql = "Delete from subscription where usrname='" + Values.CurrentUser + "' and newsid=" + self.news_id + " and time='" + self.time + "'"
            try:
                cursor.execute(sql)
            except Exception:
                connect.rollback()
            else:
                connect.commit()
                SuccBox(self, "修改成功")
                self.show_subscribe()
        else:
            sql_price = "select price from newspaper where newsid = " + self.news_id
            cursor.execute(sql_price)
            results = cursor.fetchall()
            price = results[0][0]
            pay = price * count
            unpay = usedunpay + (count - usedcount) * price
            if unpay < 0:
                unpay = 0
            curr_time = datetime.datetime.now()
            time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
            sql = "Update subscription set count=" + str(count) + ", pay=" + str(pay) + ", unpay=" + str(
                unpay) + ", updatetime='" + time_str + \
                  "' where usrname='" + Values.CurrentUser + "' and newsid=" + self.news_id + " and time='" + self.time + "'"
            try:
                cursor.execute(sql)
            except Exception as e:
                connect.rollback()
                WarningBox(self, "sql更新失败")
                print(e)
            else:
                connect.commit()
                SuccBox(self, "修改成功")
                self.show_subscribe()
        connect.close()
