import hashlib

import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, qApp

from Model.Values import Values
from Model.dataUtils import *
from View import RootInsertWindow

class RootInsert(QtWidgets.QMainWindow, RootInsertWindow.Ui_MainWindow):

    def __init__(self):
        super(RootInsert, self).__init__()
        self.setupUi(self)
        self.initial()
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def initial(self):
        self.pushButton_insert.clicked.connect(self.insert)
        self.pushButton_logout.clicked.connect(self.logout)
        self.pushButton_fresh.clicked.connect(self.show_newspaper)
        self.pushButton_up.clicked.connect(self.upshelf)
        self.pushButton_down.clicked.connect(self.downshelf)
        self.pushButton_update.clicked.connect(self.update)
        self.tableWidget.itemClicked.connect(self.select_item)
        self.show_newspaper()

    def show_newspaper(self):
        connect, cursor = sqlconn()
        sql = "Select * from newspaper"
        row = cursor.execute(sql)
        self.tableWidget.setRowCount(row)
        results = cursor.fetchall()
        for i in range(row):
            for j in range(5):
                temp_data = results[i][j]
                data = QTableWidgetItem(str(temp_data))
                self.tableWidget.setItem(i, j, data)
        connect.close()

    def logout(self):
        qApp.exit(1111)
        pass
        # Values.CurrentUser = ""
        # Values.CurrentPermission = ""
        #qApp.exit(EXIT_CODE_REBOOT)
        #self.switch_logout.emit()

    def fresh(self):
        self.show_newspaper()

    def update(self):
        news_id = str(self.lineEdit_newsid.text())
        news_name = str(self.lineEdit_newsname.text())
        price = str(self.lineEdit_price.text())
        style = str(self.comboBox_style.currentText())
        if not is_int_id(news_id) or not is_price(price) or not is_legal(news_name):
            WarningBox(self, "含有非法数据，请重试")
            return
        connect, cursor = sqlconn()
        sqltest = "select * from newspaper where newsid=" + news_id
        if cursor.execute(sqltest) > 0:
            sql = "Update newspaper set newsname='" + news_name + \
                  "', price=" + price + \
                  ", style='" + style + \
                  "' where newsid=" + news_id
            try:
                cursor.execute(sql)
            except Exception as e:
                connect.rollback()
                WarningBox(self, "sql更新失败")
                print(e)
            else:
                connect.commit()
                SuccBox(self, "修改成功")
                self.show_newspaper()
        else:
            WarningBox(self, "newsid不存在，请重试")
        connect.close()

    def select_item(self):
        select = self.tableWidget.selectedItems()
        if select:
            row = self.tableWidget.row(select[0])
            news_id = str(self.tableWidget.item(row, 0).text())
            news_name = str(self.tableWidget.item(row, 1).text())
            price = str(self.tableWidget.item(row, 2).text())
            style = str(self.tableWidget.item(row, 3).text())
            self.lineEdit_newsid.setText(news_id)
            self.lineEdit_newsname.setText(news_name)
            self.lineEdit_price.setText(price)
            self.comboBox_style.setCurrentText(style)

    def upshelf(self):
        select = self.tableWidget.selectedItems()
        if select:
            row = self.tableWidget.row(select[0])
            news_id = str(self.tableWidget.item(row, 0).text())
            sql = "Update newspaper set issell='是' where newsid=" + news_id
            connect, cursor = sqlconn()
            try:
                cursor.execute(sql)
            except Exception as e:
                connect.rollback()
                WarningBox(self, "sql更新失败")
                print(e)
            else:
                connect.commit()
                SuccBox(self, "报刊上架成功")
                self.show_newspaper()
            connect.close()
        else:
            WarningBox(self, "请先在表中选中需要上架的报刊")

    def downshelf(self):
        select = self.tableWidget.selectedItems()
        if select:
            row = self.tableWidget.row(select[0])
            news_id = str(self.tableWidget.item(row, 0).text())
            sql = "Update newspaper set issell='否' where newsid=" + news_id
            connect, cursor = sqlconn()
            try:
                cursor.execute(sql)
            except Exception as e:
                connect.rollback()
                WarningBox(self, "sql更新失败")
                print(e)
            else:
                connect.commit()
                SuccBox(self, "报刊下架成功")
                self.show_newspaper()
            connect.close()
        else:
            WarningBox(self, "请先在表中选中需要下架的报刊")

    def insert(self):
        newsid = str(self.lineEdit_newsid.text())
        newsname = str(self.lineEdit_newsname.text())
        price = str(self.lineEdit_price.text())
        style = str(self.comboBox_style.currentText())
        if is_int_id(newsid) == False or is_legal(newsname) == False or is_price(price) == False or style == "-请选择类别-":
            WarningBox(self, "非法插入，请重试！")
        else:
            connect, cursor = sqlconn()
            sqltest = "Select * from newspaper where newsid='" + newsid + "'"
            if cursor.execute(sqltest) > 0:
                WarningBox(self, "该杂志已存在，newsid冲突。")
            else:
                sql = "Insert into newspaper values (" + newsid + ",'" + newsname + "'," + price + ",'" + style + "','是')"
                try:
                    cursor.execute(sql)
                except Exception as e:
                    connect.rollback()
                    WarningBox(self, "sql插入失败")
                    print(e)
                else:
                    connect.commit()
                    SuccBox(self, "插入" + newsname + "成功！")
                    self.show_newspaper()
            connect.close()
