from selenium.webdriver.common.by import By

from pages.Page_login import txt_username, txt_password, btn_login


class stepLogin:
    def __init__(self, driver):
        self.driver = driver

    def login(self, userName, password):
        print("[Step] Login")
        self.inputUserName(userName)
        self.inputPassword(password)
        self.clickButtonLogin()

    # Action
    def inputUserName(self, email):
        print("[+] Input username")
        self.get_txtUserName().send_keys(email)

    def inputPassword(self, password):
        print("[+] Input password")
        self.get_txtPassword().send_keys(password)

    def clickButtonLogin(self):
        print("[+] Click button login")
        self.get_btnLogin().click()

    # Get element
    def get_txtUserName(self):
        return self.driver.find_element(By.XPATH, txt_username())

    def get_txtPassword(self):
        return self.driver.find_element(By.XPATH, txt_password())

    def get_btnLogin(self):
        return self.driver.find_element(By.XPATH, btn_login())
