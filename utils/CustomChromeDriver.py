from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def customChrome():
    option = Options()
    option.add_argument("--anable-extentions")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    driver.implicitly_wait(3)
    driver.maximize_window()

    print("[Open browser] Open google chrome browser")
    return driver
