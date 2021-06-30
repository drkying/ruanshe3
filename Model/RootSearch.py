import datetime

import xlwt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from Model.dataUtils import *
from Model.Values import Values
from View import RootSearchWindow


class RootSearch(QtWidgets.QMainWindow, RootSearchWindow.Ui_MainWindow):
    switch_preview = QtCore.pyqtSignal()
    switch_logout = QtCore.pyqtSignal()
    switch_back = QtCore.pyqtSignal()
    results = []
    row = 0

    def __init__(self):
        super(RootSearch, self).__init__()
        self.setupUi(self)
        self.initial()

    def initial(self):
        self.pushButton_logout.clicked.connect(self.logout)
        self.pushButton_search.clicked.connect(self.search)
        self.pushButton_print.clicked.connect(self.excel)
        self.pushButton_back.clicked.connect(self.back)

    def back(self):
        self.switch_back.emit()

    def logout(self):
        Values.CurrentUser = ""
        Values.CurrentPermission = ""
        self.switch_logout.emit()

    def search(self):
        connect, cursor = sqlconn()
        sql = "select user.name, user.dept, subscription.phone, subscription.addr, " \
              "newspaper.newsname, newspaper.price, subscription.count, subscription.pay " \
              "from user inner join subscription " \
              "on (user.usrname=subscription.usrname) " \
              "inner join newspaper " \
              "on (subscription.newsid=newspaper.newsid)"

        condition = ""
        name = str(self.lineEdit_name.text())
        if not is_legal(name):
            WarningBox(self, "姓名检索条件存在非法字符，请重试")
            self.lineEdit_name.clear()
            return

        if name != "":
            condition += ("user.name like '%" + name + "%'")

        newsname = str(self.lineEdit_newpaper.text())
        if not is_legal(newsname):
            WarningBox(self, "报刊检索条件存在非法字符，请重试")
            self.lineEdit_newpaper.clear()
            return

        if newsname != "":
            if condition != "":
                condition += " and "
            condition += ("newspaper.newsname like '%" + newsname + "%'")

        dept = str(self.comboBox_dept.currentText())
        if dept != "--请选择需要查询的部门--":
            if condition != "":
                condition += " and "
            condition += ("user.dept='" + dept + "'")

        if condition != "":
            sql += (" where " + condition)

        self.row = cursor.execute(sql)
        self.results = cursor.fetchall()
        self.show_search()
        connect.close()

    def show_search(self):
        self.tableWidget.setRowCount(self.row)
        for i in range(self.row):
            for j in range(8):
                temp_data = self.results[i][j]
                data = QTableWidgetItem(str(temp_data))
                self.tableWidget.setItem(i, j, data)

    def excel(self):
        curr_time = datetime.datetime.now()
        name = "search" + datetime.datetime.strftime(curr_time, '-%Y%m%d%H%M%S')
        default_path = 'D:/myBlog/db/print/Search/'
        file = QtWidgets.QFileDialog.getSaveFileName(self, "save", default_path + name, '.xls')

        if file[0] == "":
            return
        else:
            wb = xlwt.Workbook()
            sheet = wb.add_sheet("Search")
            sheet.write(0, 0, "name")
            sheet.write(0, 1, "dept")
            sheet.write(0, 2, "phone")
            sheet.write(0, 3, "address")
            sheet.write(0, 4, "newspaper")
            sheet.write(0, 5, "price")
            sheet.write(0, 6, "pay")

            for i in range(self.row):
                for j in range(7):
                    sheet.write(i + 1, j, self.results[i][j])

            wb.save(file[0] + file[1])
            SuccBox(self, "保存成功！\n" + file[0] + file[1])
