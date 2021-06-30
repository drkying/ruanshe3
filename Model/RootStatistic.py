from PyQt5 import QtCore, QtWidgets

from Model.dataUtils import *
from Model.Values import Values
from View import RootStatisticWindow


class RootStatistic(QtWidgets.QMainWindow, RootStatisticWindow.Ui_MainWindow):
    switch_back = QtCore.pyqtSignal()
    switch_logout = QtCore.pyqtSignal()
    switch_data = QtCore.pyqtSignal(int, dict)

    def __init__(self):
        super(RootStatistic, self).__init__()
        self.setupUi(self)
        self.initial()

    def initial(self):
        self.pushButton_statistic.clicked.connect(self.statistic)
        self.pushButton_back.clicked.connect(self.back)
        self.pushButton_logout.clicked.connect(self.logout)

    def back(self):
        self.switch_back.emit()

    def logout(self):
        Values.CurrentUser = ""
        Values.CurrentPermission = ""
        self.switch_logout.emit()

    def statistic(self):
        index = self.comboBox.currentIndex()
        connect, cursor = sqlconn()
        if index == 0:
            WarningBox(self, "请选择统计类别")
        else:
            if index == 1:
                sql = "SELECT user.name, sum(subscription.count) " \
                      "from user JOIN subscription " \
                      "on(user.usrname=subscription.usrname) " \
                      "GROUP BY  subscription.usrname"
            if index == 2:
                sql = "Select user.dept, sum(subscription.count) " \
                      "from user join subscription " \
                      "on (user.usrname=subscription.usrname) " \
                      "group by user.dept"
            if index == 3:
                sql = "Select newspaper.newsname, sum(subscription.count) " \
                      "from newspaper join subscription " \
                      "on (newspaper.newsid=subscription.newsid) " \
                      "group by newspaper.newsid"
            if index == 4:
                sql = "Select newspaper.style, sum(subscription.count) " \
                      "from newspaper join subscription " \
                      "on (newspaper.newsid=subscription.newsid) " \
                      "group by newspaper.style"
            cursor.execute(sql)
            results = cursor.fetchall()
            data = dict()
            for result in results:
                data[result[0]] = int(result[1])

            self.switch_data.emit(index, data)
        connect.close()
