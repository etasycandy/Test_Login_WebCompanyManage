import unittest

from parameterized import parameterized

from steps.ReadDataTest import readDatatest
from steps.Step_login import stepLogin
from steps.Step_addComp import stepAddComp
from utils.CustomChromeDriver import customChrome
from verifys.Verify_login import verifyLogin

dataTestLogin = readDatatest().dataTestLogin()
dataTestAddComp = readDatatest().dataTestAddComp()


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("========== [BEGIN TEST] ==========")
        self.browser = customChrome()
        self.browser.get("http://localhost:3000/auth/login")

    def tearDown(self):
        self.browser.quit()
        print("========== [END TEST] ========== \n")

    @parameterized.expand(dataTestLogin)
    def test_login(self, no, username, password, desiredResult, desiredMessage):
        stepLogin(self.browser).login(username, password)
        self.assertIn(desiredMessage, verifyLogin(self.browser).login())

    @parameterized.expand(dataTestAddComp)
    def test_add_company(self, no, username, password, name, email, address, reviews, desiredMessage):
        stepLogin(self.browser).login(username, password)
        stepAddComp(self.browser).addComp(name, email, address, reviews)
        print("Complete!")
        # self.assertIn(desiredMessage)


if __name__ == '__main__':
    unittest.main()
