from PyQt5.QtWidgets import QMessageBox
import pymysql


def sqlconn():
    connect = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="hityys123",
        database="Subscribe",
        autocommit=True
    )
    cursor = connect.cursor()
    return connect, cursor


def WarningBox(c, info):
    c.box = QMessageBox(QMessageBox.Warning, "Failed", info)
    yes = c.box.addButton('确定', QMessageBox.YesRole)
    c.box.setIcon(2)
    c.box.show()


def SuccBox(c, info):
    c.box = QMessageBox(QMessageBox.Information, "Success", info)
    yes = c.box.addButton('ok', QMessageBox.YesRole)
    c.box.setIcon(1)
    c.box.show()


def is_legal(info):
    if "'" in info or '"' in info or '%' in info or '/' in info:
        return False
    return True


def is_int_id(id):
    try:
        if int(id) > 0:
            return True
        else:
            return False
    except Exception:
        return False
