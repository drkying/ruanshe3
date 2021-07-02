# coding:utf-8


from PyQt5 import QtCore, QtGui, QtWidgets, sip

import sys

import qtawesome
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget

from Model.BackupRecover import BackRecover
from Model.Login import Login
from Model.Menu import Menu
from Model.Register import Register
from Model.RootInsert import RootInsert
from Model.RootSearch import RootSearch
from Model.RootStatistic import RootStatistic
from Model.Statistic import Statistic
from Model.UserAddAddr import UserAddAddr
from Model.UserAddr import UserAddr
from Model.UserInfo import UserInfo
from Model.UserManage import UserManager
from Model.UserSettle import UserSettle
from Model.UserSubscribe import UserSubscribe
from Model.dataUtils import getRecommend, getSearchResult


class MainUi(QtWidgets.QMainWindow):
    recommend = set()

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.addLeft()
        self.addRight()
        self.improveUi()
        self.left_close.clicked.connect(self.close)

    def init_ui(self):
        # self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格
        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_layout.setAlignment(Qt.AlignTop)
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格
        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

    def addLeft(self):
        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.left_label_1 = QtWidgets.QPushButton("首页")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("普通用户")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("管理员")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "搜索推荐")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.music', color='white'), "订阅报刊")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.sellsy', color='white'), "订阅管理")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.film', color='white'), "金额结算")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.home', color='white'), "地址管理")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.download', color='white'), "报刊管理")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.heart', color='white'), "订阅查询")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "订阅统计")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "数据维护")
        self.left_button_9.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)

        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)

        self.left_layout.addWidget(self.left_label_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)

        self.left_layout.addWidget(self.left_label_3, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

    def addRight(self):
        self.right_bar_widget = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '搜索  ')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right_bar_widget_search_input.setPlaceholderText("输入报刊名，回车进行搜索")
        self.right_bar_widget_search_input.returnPressed.connect(self.showSearchResult)
        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right_bar_layout.addWidget(self.right_bar_widget_search_input, 0, 1, 1, 8)
        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)

        self.right_recommend_label = QtWidgets.QLabel("杂志推荐")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        temp = list(getRecommend(5))
        for i in range(5):
            recommend_button = QtWidgets.QToolButton()
            recommend_button.setText(temp[i][1])
            recommend_button.setIcon(QtGui.QIcon('./img.png'))  # 设置按钮图标
            recommend_button.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
            recommend_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文
            self.right_recommend_layout.addWidget(recommend_button, 0, i)

        self.right_layout.addWidget(self.right_recommend_label, 1, 0, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)

    def improveUi(self):
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
            QWidget#left_widget{
                background:gray;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
        ''')

        self.right_bar_widget_search_input.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.right_recommend_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框

        self.main_layout.setSpacing(0)

    def clearRight(self):
        for i in range(self.right_layout.count()):
            self.right_layout.itemAt(i).widget().deleteLater()

    # def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
    #     self._endPos = e.pos() - self._startPos
    #     self.move(self.pos() + self._endPos)
    #
    # def mousePressEvent(self, e: QMouseEvent):
    #     if e.button() == Qt.LeftButton:
    #         self._isTracking = True
    #         self._startPos = QPoint(e.x(), e.y())
    #
    # def mouseReleaseEvent(self, e: QMouseEvent):
    #     if e.button() == Qt.LeftButton:
    #         self._isTracking = False
    #         self._startPos = None
    #         self._endPos = None

    def showSearchResult(self):
        s = self.right_bar_widget_search_input.text()
        self.clearRight()

        self.right_bar_widget = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '搜索  ')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right_bar_widget_search_input.setPlaceholderText(s)
        self.right_bar_widget_search_input.returnPressed.connect(self.showSearchResult)
        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right_bar_layout.addWidget(self.right_bar_widget_search_input, 0, 1, 1, 8)
        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)

        self.right_recommend_label = QtWidgets.QLabel("搜索结果")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        results = getSearchResult(s)
        for i in range(len(results)):
            recommend_button = QtWidgets.QToolButton()
            recommend_button.setText(results[i][1])
            recommend_button.setIcon(QtGui.QIcon('./img.png'))  # 设置按钮图标
            recommend_button.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
            recommend_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文
            self.right_recommend_layout.addWidget(recommend_button, 0, i)

        self.right_layout.addWidget(self.right_recommend_label, 1, 0, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)


def showit(a, b):
    global x
    if b == 1:
        a.clearRight()
        a.addRight()
        return

    elif b == 2:
        x = eval('UserSubscribe()')
    elif b == 3:
        x = eval('UserManager()')
    elif b == 4:
        x = eval('UserSettle()')
    elif b == 5:
        x = eval('UserAddr()')

    elif b == 6:
        x = eval('RootInsert()')
    elif b == 7:
        x = eval('RootSearch()')
    elif b == 8:
        x = eval('RootStatistic()')
    elif b == 9:
        x = eval('BackRecover()')
    if b is not None:
        a.clearRight()
        a.right_layout.addWidget(x, 2, 0)


def main():
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.resize(1000, 600)

    gui.left_button_1.clicked.connect(
        lambda: (showit(gui, 1))
    )
    gui.left_button_2.clicked.connect(
        lambda: (showit(gui, 2)))
    gui.left_button_3.clicked.connect(
        lambda: (showit(gui, 3)))
    gui.left_button_4.clicked.connect(
        lambda: (showit(gui, 4)))
    gui.left_button_5.clicked.connect(
        lambda: (showit(gui, 5)))
    gui.left_button_6.clicked.connect(
        lambda: (showit(gui, 6)))
    gui.left_button_7.clicked.connect(
        lambda: (showit(gui, 7)))
    gui.left_button_8.clicked.connect(
        lambda: (showit(gui, 8)))
    gui.left_button_9.clicked.connect(
        lambda: (showit(gui, 9)))

    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
