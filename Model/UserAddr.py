import qdarkstyle
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from Model.Values import Values
from Model.dataUtils import *
from View import UserAddrWindow


class UserAddr(QtWidgets.QMainWindow, UserAddrWindow.Ui_MainWindow):
    switch_add_addr = QtCore.pyqtSignal()

    def __init__(self):
        super(UserAddr, self).__init__()
        self.setupUi(self)
        self.initial()
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def initial(self):
        self.show_addr()
        self.pushButton_update.clicked.connect(self.table_update)
        self.pushButton_add.clicked.connect(self.add_addr)
        self.pushButton_delete.clicked.connect(self.delete)
        self.pushButton_refresh.clicked.connect(self.show_addr)
        self.tableWidget.itemClicked.connect(self.set_line_text)

    def add_addr(self):
        self.switch_add_addr.emit()

    def show_addr(self):
        connect, cursor = sqlconn()
        sql = "select phone, addr from address where usrname='" + Values.CurrentUser + "'"
        row = cursor.execute(sql)
        self.tableWidget.setRowCount(row)
        results = cursor.fetchall()
        for i in range(row):
            for j in range(2):
                temp_data = results[i][j]
                data = QTableWidgetItem(str(temp_data))
                self.tableWidget.setItem(i, j, data)
        connect.close()

    def set_line_text(self):
        select = self.tableWidget.selectedItems()
        if select:
            row = self.tableWidget.row(select[0])
            colomn = self.tableWidget.column(select[0])
            text = str(self.tableWidget.item(row, colomn).text())
            self.lineEdit.setText(text)

    def table_update(self):
        select = self.tableWidget.selectedItems()
        if select:
            row = self.tableWidget.row(select[0])
            phone = str(self.tableWidget.item(row, 0).text())
            addr = str(self.tableWidget.item(row, 1).text())
            colomn = self.tableWidget.column(select[0])
            connect, cursor = sqlconn()
            if colomn == 0:
                new_phone = str(self.lineEdit.text())
                if new_phone == "" or is_legal(new_phone) == False:
                    WarningBox(self, "手机号不可为空或存在非法字符，请重试")
                    self.lineEdit.clear()
                    return
                else:
                    sql_test = "Select * from address where usrname='" + Values.CurrentUser + "' and phone='" + new_phone + "' and addr='" + addr + "'"
                    if cursor.execute(sql_test) > 0:
                        WarningBox(self, "修改后的记录已存在，请重试")
                        self.lineEdit.clear()
                        return
                    else:
                        sql = "Update address set phone='" + new_phone + "' where usrname='" + Values.CurrentUser + "' and phone='" + phone + "' and addr='" + addr + "'"
            elif colomn == 1:
                new_addr = str(self.lineEdit.text())
                if new_addr == "" or is_legal(new_addr) == False:
                    WarningBox(self, "地址不可为空或存在非法字符，请重试")
                    self.lineEdit.clear()
                    return
                else:
                    sql_test = "Select * from address where usrname='" + Values.CurrentUser + "' and phone='" + phone + "' and addr='" + new_addr + "'"
                    if cursor.execute(sql_test) > 0:
                        WarningBox(self, "修改后的记录已存在，请重试")
                        self.lineEdit.clear()
                        return
                    else:
                        sql = "Update address set addr='" + new_addr + "' where usrname='" + Values.CurrentUser + "' and phone='" + phone + "' and addr='" + addr + "'"
            try:
                cursor.execute(sql)
            except Exception as e:
                print(e)
                connect.rollback()
                WarningBox(self, "修改失败，请重试")
            else:
                connect.commit()
                SuccBox(self, "修改成功")
                self.show_addr()
            connect.close()
        else:
            WarningBox(self, "请选中需要修改的内容")

    def delete(self):
        select = self.tableWidget.selectedItems()
        if select:
            row = self.tableWidget.row(select[0])
            phone = str(self.tableWidget.item(row, 0).text())
            addr = str(self.tableWidget.item(row, 1).text())
            connect, cursor = sqlconn()
            sqlcount = "select * from address where usrname='" + Values.CurrentUser + "'"
            count = cursor.execute(sqlcount)
            if count == 1:
                WarningBox(self, "当前仅有一条地址记录，不允许删除该条记录")
            else:
                sql = "Delete from address where usrname='" + Values.CurrentUser + "' and phone='" + phone + "' and addr='" + addr + "'"
                try:
                    cursor.execute(sql)
                except Exception as e:
                    connect.rollback()
                    WarningBox(self, "删除地址失败，请重试")
                    print(e)
                else:
                    SuccBox(self, "删除地址成功")
                    connect.commit()
                    self.show_addr()
            connect.close()
        else:
            WarningBox(self, "请选中需要删除的地址")
