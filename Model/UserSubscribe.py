import datetime

import qdarkstyle
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from Model.dataUtils import *
from Model.Values import Values
from View import UserSubscribeWindow


class UserSubscribe(QtWidgets.QMainWindow, UserSubscribeWindow.Ui_MainWindow):
    switch_add_addr = QtCore.pyqtSignal()

    def __init__(self):
        super(UserSubscribe, self).__init__()
        self.setupUi(self)
        self.initial()
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def initial(self):
        self.pushButton_subscribe.clicked.connect(self.subscribe)
        self.pushButton_fresh.clicked.connect(self.show_subscribe)
        self.pushButton_fresh.clicked.connect(self.show_address)
        self.pushButton_fresh.clicked.connect(self.show_newspaper)
        self.show_newspaper()
        self.show_subscribe()
        self.show_address()
        self.show_news_id()
        self.comboBox_addr.activated.connect(self.is_add)
        self.tableWidget_newspaper.itemClicked.connect(self.set_news_id)

    def setGui(self, gui):
        self.gui = gui

    def is_add(self):
        addr = str(self.comboBox_addr.currentText())
        if addr == "如果未添加地址，请到地址管理中添加":
            self.switch_add_addr.emit()
        else:
            pass

    def boxitem(self, results):
        combo = []
        for result in results:
            temp_str = str(result[0]) + "-" + str(result[1])
            combo.append(temp_str)
        return combo

    def set_news_id(self):
        select = self.tableWidget_newspaper.selectedItems()
        if select:
            row = self.tableWidget_newspaper.row(select[0])
            new_id = str(self.tableWidget_newspaper.item(row, 0).text())
            news_name = str(self.tableWidget_newspaper.item(row, 1).text())
            self.comboBox_newsid.setCurrentText(new_id + "-" + news_name)

    def show_address(self):
        self.comboBox_addr.clear()
        connect, cursor = sqlconn()
        sql = "Select phone, addr from address where usrname='" + Values.CurrentUser + "'"
        cursor.execute(sql)
        results = cursor.fetchall()
        combo = self.boxitem(results)
        self.comboBox_addr.addItem("--请选择订阅地址--")
        self.comboBox_addr.addItems(combo)
        self.comboBox_addr.addItem("如果未添加地址，请到地址管理中添加")
        connect.close()

    def show_news_id(self):
        self.comboBox_newsid.clear()
        connect, cursor = sqlconn()
        sql = "Select newsid, newsname from newspaper where issell='是'"
        cursor.execute(sql)
        results = cursor.fetchall()
        combo = self.boxitem(results)
        self.comboBox_newsid.addItem("--请选择需要订阅的报刊--")
        self.comboBox_newsid.addItems(combo)
        connect.close()

    def show_newspaper(self):
        connect, cursor = sqlconn()
        sql = "Select * from newspaper where issell='是'"
        row = cursor.execute(sql)
        self.tableWidget_newspaper.setRowCount(row)
        results = cursor.fetchall()
        for i in range(row):
            for j in range(4):
                temp_data = results[i][j]
                data = QTableWidgetItem(str(temp_data))
                self.tableWidget_newspaper.setItem(i, j, data)
        connect.close()

    def show_subscribe(self):
        connect, cursor = sqlconn()
        sql = "select user.name, newspaper.newsname, newspaper.price, subscription.pay, subscription.unpay, " \
              "subscription.phone, subscription.addr, subscription.time " \
              "from user inner join subscription " \
              "on (user.usrname=subscription.usrname) " \
              "inner join newspaper " \
              "on (subscription.newsid=newspaper.newsid) " \
              "where user.usrname='" + Values.CurrentUser + "'"
        row = cursor.execute(sql)
        self.tableWidget_subscribe.setRowCount(row)
        self.tableWidget_subscribe.setColumnWidth(7, 180)
        results = cursor.fetchall()
        for i in range(row):
            for j in range(8):
                temp_data = results[i][j]
                data = QTableWidgetItem(str(temp_data))
                self.tableWidget_subscribe.setItem(i, j, data)
        connect.close()

    def subscribe(self):
        newsid = str(self.comboBox_newsid.currentText()).split('-')[0]
        count = self.spinBox_count.value()
        address = str(self.comboBox_addr.currentText())
        phone = address.split('-', 1)[0]
        addr = address.split('-', 1)[1]

        if is_int_id(newsid) == False or count == 0 or address == "--请选择订阅地址--" or address == "如果未添加地址，请到地址管理中添加":
            WarningBox(self, "订阅信息不完整，请补全订阅信息！")
            return
        connect, cursor = sqlconn()

        sql_price = "select price from newspaper where newsid = " + newsid
        cursor.execute(sql_price)
        results = cursor.fetchall()
        price = results[0][0]
        pay = price * count
        curr_time = datetime.datetime.now()
        time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')

        sql = "Insert into subscription values ('" + Values.CurrentUser + "'," + newsid + "," + str(
            count) + "," + str(pay) + "," + str(pay) + ",'" + phone + "','" + addr + "','" + time_str + "', NULL)"
        try:
            cursor.execute(sql)
        except Exception as e:
            connect.rollback()
            WarningBox(self, "sql插入或更新失败")
            print(e)
        else:
            connect.commit()
            SuccBox(self, "订阅成功")
            self.show_subscribe()
        connect.close()
