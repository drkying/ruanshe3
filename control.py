from Model.Login import Login
from Model.Register import Register


class Controller:
    def __init__(self):
        pass

    def ShowLoginWindow(self):
        self.LoginWindow = Login()
        self.LoginWindow.show()
        self.LoginWindow.switch_register.connect(self.ShowRegisterWindow)
        self.LoginWindow.switch_register.connect(self.LoginWindow.close)
        # self.LoginWindow.switch_login.connect(self.ShowMenu)
        self.LoginWindow.switch_login.connect(self.LoginWindow.close)

    def ShowRegisterWindow(self):
        self.RegisterWindow = Register()
        self.RegisterWindow.show()
        self.RegisterWindow.switch_back.connect(self.ShowLoginWindow)
        self.RegisterWindow.switch_back.connect(self.RegisterWindow.close)
