from PyQt5 import QtWidgets
from PyQt5 import QtCore
import sys
from Controller import Controller

if __name__ == "__main__":
    try:
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        app = QtWidgets.QApplication(sys.argv)
        control = Controller()
        control.ShowLoginWindow()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
