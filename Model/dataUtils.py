import random
import time

from PyQt5.QtWidgets import QMessageBox
import pymysql

from Model.Values import Values

recommendList = []


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


def is_price(price):
    try:
        if float(price) > 0:
            return True
        else:
            return False
    except Exception:
        return False


def getRecommend(n):
    connect, cursor = sqlconn()
    sql = "select newsid,newsname from newspaper where style in (" \
          "select style from newspaper where newsid in (" \
          "select newsid from subscription where usrname = '%s'))" % (
              Values.CurrentUser)
    cursor.execute(sql)
    results = cursor.fetchall()
    for s in results:
        recommendList.append(s)

    if n > len(recommendList):
        return recommendList

    temp = set()
    for i in range(0, n):
        index = random.randint(0, len(recommendList) - 1)
        if recommendList[index] not in temp:
            temp.add(recommendList[index])
        if i == n - 1 and len(temp) < n:
            temp |= getRecommend(n)

    return temp


def getSearchResult(s):
    connect, cursor = sqlconn()
    sql = "select newsid,newsname from newspaper where newsname like '%%%s%%'" % s
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    return results

# getSearchResult("少年")
