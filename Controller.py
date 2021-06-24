from Model.BackupRecover import BackRecover
from Model.Login import Login
from Model.Menu import Menu
from Model.Register import Register
from Model.RootInsert import RootInsert


class Controller:
    def __init__(self):
        pass

    def ShowLoginWindow(self):
        self.LoginWindow = Login()
        self.LoginWindow.show()
        self.LoginWindow.switch_register.connect(self.ShowRegisterWindow)
        self.LoginWindow.switch_register.connect(self.LoginWindow.close)
        self.LoginWindow.switch_login.connect(self.ShowMenu)
        self.LoginWindow.switch_login.connect(self.LoginWindow.close)

    def ShowRegisterWindow(self):
        self.RegisterWindow = Register()
        self.RegisterWindow.show()
        self.RegisterWindow.switch_back.connect(self.ShowLoginWindow)
        self.RegisterWindow.switch_back.connect(self.RegisterWindow.close)

    def ShowMenu(self):
        self.Menu = Menu()
        self.Menu.show()
        self.Menu.switch_logout.connect(self.ShowLoginWindow)
        self.Menu.switch_logout.connect(self.Menu.close)
        # self.Menu.switch_user_info.connect(self.ShowUserInfo)
        # self.Menu.switch_user_subscribe.connect(self.ShowUserSubscribe)
        # self.Menu.switch_user_subscribe.connect(self.Menu.close)
        # self.Menu.switch_user_manage.connect(self.ShowUserManage)
        # self.Menu.switch_user_manage.connect(self.Menu.close)
        # self.Menu.switch_user_settle.connect(self.ShowUserSettle)
        # self.Menu.switch_user_settle.connect(self.Menu.close)
        # self.Menu.switch_user_addr.connect(self.ShowUserAddr)
        # self.Menu.switch_user_addr.connect(self.Menu.close)
        #
        # self.Menu.switch_root_search.connect(self.ShowRootSearch)
        # self.Menu.switch_root_search.connect(self.Menu.close)
        self.Menu.switch_root_insert.connect(self.ShowRootInsert)
        self.Menu.switch_root_insert.connect(self.Menu.close)
        # self.Menu.switch_root_statistics.connect(self.ShowRootStatistic)
        # self.Menu.switch_root_statistics.connect(self.Menu.close)
        self.Menu.switch_root_backup.connect(self.ShowRootBackup)
        self.Menu.switch_root_backup.connect(self.Menu.close)

    def ShowRootInsert(self):
        self.RootInsert = RootInsert()
        self.RootInsert.show()
        self.RootInsert.switch_back.connect(self.ShowMenu)
        self.RootInsert.switch_back.connect(self.RootInsert.close)
        self.RootInsert.switch_logout.connect(self.ShowLoginWindow)
        self.RootInsert.switch_logout.connect(self.RootInsert.close)

    def ShowRootBackup(self):
        self.RootBackup = BackRecover()
        self.RootBackup.show()

        self.RootBackup.switch_back.connect(self.ShowMenu)
        self.RootBackup.switch_back.connect(self.RootBackup.close)
        self.RootBackup.switch_logout.connect(self.ShowLoginWindow)
        self.RootBackup.switch_logout.connect(self.RootBackup.close)
