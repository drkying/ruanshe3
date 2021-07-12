import os
import datetime

import qdarkstyle
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets
from matplotlib import pyplot as plt
import matplotlib as mpl
import shutil
from Model.dataUtils import *
from View import StatisticGraph


class Statistic(QtWidgets.QMainWindow, StatisticGraph.Ui_MainWindow):
    index = 0
    data = {}
    figure = plt.figure("pymatplotlib")
    ax = figure.gca()
    canvas = FigureCanvas(figure)
    title = "Statistic By "
    fname = ""
    xlabel = ""

    def __init__(self, index, data):
        super(Statistic, self).__init__()
        self.setupUi(self)
        self.index = index
        self.data = data
        self.initial()
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def initial(self):
        self.verticalLayout.addWidget(self.canvas)
        self.pushButton_print.clicked.connect(self.print)
        if self.index == 1:
            self.title = self.title + "Name"
            self.xlabel = "Name"
        elif self.index == 2:
            self.title = self.title + "Department"
            self.xlabel = "Department"
        elif self.index == 3:
            self.title = self.title + "News Name"
            self.xlabel = "Newspaper Name"
        elif self.index == 4:
            self.title = self.title + "News Style"
            self.xlabel = "Newspaper Style"
        self.showGraph()

    def print(self):
        curr_time = datetime.datetime.now()
        name = self.title + datetime.datetime.strftime(curr_time, '-%Y%m%d%H%M%S')
        default_path = 'D:/myBlog/db/print/Statistic/'
        file = QtWidgets.QFileDialog.getSaveFileName(self, "save", default_path + name, '.png')

        if file[0] != "":
            os.chdir("D:/myBlog/db/cache/")
            if os.path.exists(self.fname):
                shutil.copyfile(self.fname, file[0] + file[1])
                if os.path.exists(file[0] + file[1]):
                    SuccBox(self, "保存成功，" + file[0] + file[1])
                    return
            WarningBox(self, "保存失败")

    def showGraph(self):
        self.ax.clear()
        mpl.rcParams['font.sans-serif'] = ['SimHei']
        mpl.rcParams['axes.unicode_minus'] = False
        x_axis = tuple(self.data.keys())
        print(tuple(self.data.keys()))
        y_axis = tuple(self.data.values())
        for a, b in self.data.items():
            self.ax.text(a, b + 0.1, '%.0f' % b, ha='center', va='bottom', fontsize=11)
        self.ax.bar(x_axis, y_axis, color='cyan')

        self.ax.set_xticklabels(x_axis, rotation=-20)

        self.ax.set_xlabel(self.xlabel, ha='right', va="top")  # 指定x轴描述信息
        self.ax.set_ylabel(r"Subscription")  # 指定y轴描述信息
        self.ax.set_title(label=self.title)
        temp = max(self.data.values())
        if temp % 100 > 49:
            ylim = (temp // 100 + 2) * 100
        else:
            ylim = (temp // 100 + 1) * 100
        self.ax.set_ylim(0, ylim)
        curr_time = datetime.datetime.now()
        self.fname = self.title + datetime.datetime.strftime(curr_time, '-%Y%m%d%H%M%S') + ".png"
        os.chdir("D:/myBlog/db/cache")
        plt.savefig(self.fname)
        self.canvas.draw()

    def closeEvent(self, QCloseEvent):
        os.chdir("D:/myBlog/db/cache")
        os.remove(self.fname)
