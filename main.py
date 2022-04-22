import unittest

from parameterized import parameterized

from steps.ReadDataTest import readDatatest
from steps.Step_login import stepLogin
from utils.CustomChromeDriver import customChrome
from verifys.Verify_login import verifyLogin

dataTest = readDatatest().dataTestLogin()


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("========== [BEGIN TEST] ==========")
        self.browser = customChrome()
        self.browser.get("http://localhost:3000/auth/login")

    def tearDown(self):
        self.browser.quit()
        print("========== [END TEST] ========== \n")

    @parameterized.expand(dataTest)
    def test_login(self, no, username, password, desiredResult, desiredMessage):
        stepLogin(self.browser).login(username, password)
        self.assertIn(desiredMessage, verifyLogin(self.browser).login())


if __name__ == '__main__':
    unittest.main()
