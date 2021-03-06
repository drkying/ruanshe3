from Model.BackupRecover import BackRecover
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


class Controller:
    def __init__(self):
        pass


    def ShowRegisterWindow(self):
        self.RegisterWindow = Register()
        self.RegisterWindow.show()
        self.RegisterWindow.switch_back.connect(self.ShowLoginWindow)
        self.RegisterWindow.switch_back.connect(self.RegisterWindow.close)

    def ShowRootInsert(self):
        self.RootInsert = RootInsert()
        self.RootInsert.show()
        self.RootInsert.switch_back.connect(self.RootInsert.close)
        self.RootInsert.switch_logout.connect(self.ShowLoginWindow)
        self.RootInsert.switch_logout.connect(self.RootInsert.close)

    def ShowRootBackup(self):
        self.RootBackup = BackRecover()
        self.RootBackup.show()

        self.RootBackup.switch_back.connect(self.RootBackup.close)
        self.RootBackup.switch_logout.connect(self.ShowLoginWindow)
        self.RootBackup.switch_logout.connect(self.RootBackup.close)

    def ShowUserSubscribe(self):
        self.UserSubscribe = UserSubscribe()
        self.UserSubscribe.show()
        self.UserSubscribe.switch_back.connect(self.UserSubscribe.close)
        self.UserSubscribe.switch_add_addr.connect(self.ShowUserAddAddr)
        self.UserSubscribe.switch_logout.connect(self.ShowLoginWindow)
        self.UserSubscribe.switch_logout.connect(self.UserSubscribe.close)

    def ShowUserInfo(self):
        self.UserInfo = UserInfo()
        self.UserInfo.show()
        self.UserInfo.switch_logout.connect(self.ShowLoginWindow)
        self.UserInfo.switch_logout.connect(self.UserInfo.close)

    def ShowUserAddr(self):
        self.UserAddr = UserAddr()
        self.UserAddr.show()

        self.UserAddr.switch_add_addr.connect(self.ShowUserAddAddr)
        self.UserAddr.switch_back.connect(self.UserAddr.close)
        self.UserAddr.switch_logout.connect(self.ShowLoginWindow)
        self.UserAddr.switch_logout.connect(self.UserAddr.close)

    def ShowUserAddAddr(self, pre):
        self.UserAddAddr = UserAddAddr(pre)
        self.UserAddAddr.show()
        if pre == 1:
            self.UserAddAddr.switch_to_manage.connect(self.UserAddAddr.close)
            self.UserAddAddr.switch_to_manage.connect(self.UserAddr.show_addr)
        if pre == 2:
            self.UserAddAddr.switch_to_subscribe.connect(self.UserAddAddr.close)
            self.UserAddAddr.switch_to_subscribe.connect(self.UserSubscribe.show_address)

    def ShowUserManage(self):
        self.UserManage = UserManager()
        self.UserManage.show()
        self.UserManage.switch_back.connect(self.UserManage.close)
        self.UserManage.switch_logout.connect(self.ShowLoginWindow)
        self.UserManage.switch_logout.connect(self.UserManage.close)

    def ShowUserSettle(self):
        self.UserSettle = UserSettle()
        self.UserSettle.show()
        self.UserSettle.switch_back.connect(self.UserSettle.close)
        self.UserSettle.switch_logout.connect(self.ShowLoginWindow)
        self.UserSettle.switch_logout.connect(self.UserSettle.close)

    def ShowRootSearch(self):
        self.RootSearch = RootSearch()
        self.RootSearch.show()
        self.RootSearch.switch_back.connect(self.RootSearch.close)
        self.RootSearch.switch_logout.connect(self.ShowLoginWindow)
        self.RootSearch.switch_logout.connect(self.RootSearch.close)

    def ShowRootStatistic(self):
        self.RootStatistic = RootStatistic()
        self.RootStatistic.show()

        self.RootStatistic.switch_data.connect(self.ShowStatisticGraph)
        self.RootStatistic.switch_back.connect(self.RootStatistic.close)
        self.RootStatistic.switch_logout.connect(self.ShowLoginWindow)
        self.RootStatistic.switch_logout.connect(self.RootStatistic.close)

    def ShowStatisticGraph(self, index, data):
        self.Statistic = Statistic(index, data)
        self.Statistic.show()
