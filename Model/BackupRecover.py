import os
import datetime

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from Model.Values import Values
from Model.dataUtils import *
from View import BackupRecoverWindow


class BackRecover(QtWidgets.QMainWindow, BackupRecoverWindow.Ui_MainWindow):
    switch_back = QtCore.pyqtSignal()
    switch_logout = QtCore.pyqtSignal()

    def __init__(self):
        super(BackRecover, self).__init__()
        self.setupUi(self)
        self.initial()

    def initial(self):
        self.show_backup()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pushButton_backup.clicked.connect(self.backup)
        self.pushButton_recover.clicked.connect(self.recover)
        self.pushButton_back.clicked.connect(self.back)
        self.pushButton_logout.clicked.connect(self.logout)

    def back(self):
        self.switch_back.emit()

    def logout(self):
        Values.CurrentUser = ""
        Values.CurrentPermission = ""
        self.switch_logout.emit()

    def show_backup(self):
        filename = list()
        back_time = list()
        path = os.getcwd() + '/backup'
        if os.path.exists(path):
            for root, dirs, files in os.walk(os.getcwd()):
                for file in files:
                    if file.endswith(".sql"):
                        fname = file.split('.')[0]
                        time_str = fname.split('-')[1]
                        curr_time = datetime.datetime.strptime(time_str, '%Y%m%d%H%M%S')
                        time_str = datetime.datetime.strftime(curr_time, '%Y-%m-%d %H:%M:%S')
                        filename.append(fname.split('-')[0])
                        back_time.append(time_str)
            row = len(filename)
            if row != 0:
                self.tableWidget.setRowCount(row)
                for i in range(row):
                    temp_data = filename[i]
                    data = QTableWidgetItem(str(temp_data))
                    self.tableWidget.setItem(i, 0, data)
                    temp_data = back_time[i]
                    data = QTableWidgetItem(str(temp_data))
                    self.tableWidget.setItem(i, 1, data)
                self.tableWidget.sortItems(1, QtCore.Qt.DescendingOrder)
            else:
                self.tableWidget.setRowCount(1)
                data = QTableWidgetItem("暂无备份")
                self.tableWidget.setItem(1, 0, data)
                self.tableWidget.setItem(1, 1, data)
                WarningBox(self, "默认路径backup下未找到备份文件")
        else:
            os.mkdir(path)
            self.show_backup()

    def backup(self):
        curr_time = datetime.datetime.now()
        name = datetime.datetime.strftime(curr_time, '-%Y%m%d%H%M%S')
        default_path = 'D:/myBlog/ruanshe3/backup/'
        file = QtWidgets.QFileDialog.getSaveFileName(self, "save", default_path + "backup", '.sql')
        if file[0] != "":
            filename = file[0] + name + ".sql"
            command = "mysqldump -u root --password=hityys123 subscribe > " + filename
            os.system(command)
            SuccBox(self, "备份成功, " + filename)
            self.show_backup()

    def recover(self):
        default_path = "D:/myBlog/ruanshe3/backup/"
        file = QtWidgets.QFileDialog.getOpenFileName(self, "recover", default_path, '*.sql')
        if file[0] != "":
            command = "mysql -u root --password=hityys123 subscribe < " + file[0]
            os.system(command)
            SuccBox(self, "恢复备份成功")
            return
        WarningBox(self, "恢复失败")
