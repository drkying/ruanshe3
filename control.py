import model


class Controller:
    def __init__(self):
        pass

    def ShowLoginWindow(self):
        self.LoginWindow=model.Login()
        self.LoginWindow.show()
        #self.LoginWindow.switch_register.connect(self.LoginWindow.close)
        #self.LoginWindow.switch_login.connect(self.LoginWindow.close)
