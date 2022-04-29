from selenium.webdriver.common.by import By

from pages.Page_company import btn_companyMenu, btn_addCompany, txt_compName, txt_compEmail, txt_compAddress, \
    txt_compLogo, txt_compReview, btn_compSubmit


class stepAddComp:
    def __init__(self, driver):
        self.driver = driver

    # Get element
    def get_btnCompanyMenu(self):
        return self.driver.find_element(By.XPATH, btn_companyMenu())

    def get_btnAddCompany(self):
        return self.driver.find_element(By.XPATH, btn_addCompany())

    def get_txtCompName(self):
        return self.driver.find_element(By.XPATH, txt_compName())

    def get_txtCompEmail(self):
        return self.driver.find_element(By.XPATH, txt_compEmail())

    def get_txtCompAddress(self):
        return self.driver.find_element(By.XPATH, txt_compAddress())

    def get_txtCompLogo(self):
        return self.driver.find_element(By.XPATH, txt_compLogo())

    def get_txtCompReview(self):
        return self.driver.find_element(By.XPATH, txt_compReview())

    def get_btnCompSubmit(self):
        return self.driver.find_element(By.XPATH, btn_compSubmit())

    # Action
    def clickCompMenu(self):
        print("[+] Click button Company on menu")
        self.get_btnCompanyMenu().click()

    def clickAddComp(self):
        print("[+] Click button Add company")
        self.get_btnAddCompany().click()

    def inputCompName(self, compName):
        print("[+] Input Name company")
        self.get_txtCompName().send_keys(compName)

    def inputCompEmail(self, email):
        print("[+] Input Email company")
        self.get_txtCompEmail().send_keys(email)

    def inputCompAddress(self, address):
        print("[+] Input Address company")
        self.get_txtCompAddress().send_keys(address)

    def inputCompLogo(self):
        print("[+] Input Logo company")
        # self.get_txtCompLogo().click()
        # Runtime.getRuntime().exec("D:\Tester\scriptUploadFile.exe");

    def inputCompReview(self, review):
        print("[+] Input Review company")
        self.get_txtCompReview().send_keys(review)

    def clickButtonSubmit(self):
        print("[+] Click button Submit")
        self.get_btnCompSubmit().click()

    def addComp(self, name, email, address, reviews):
        print("[Step] Add Company")
        self.clickCompMenu()
        self.clickAddComp()
        self.inputCompName(name)
        self.inputCompEmail(email)
        self.inputCompAddress(address)
        self.inputCompLogo()
        self.inputCompReview(reviews)
        self.clickButtonSubmit()
