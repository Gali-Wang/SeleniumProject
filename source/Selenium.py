from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


def setBrowser():
    option = Options()
    option.add_experimental_option("detach", True)
    #option.add_argument("--no-sandbox")

    browser = webdriver.Chrome(options=option)
    return browser

browser = setBrowser()
browser.get("https://www.baidu.com")
time.sleep(3)
browser.maximize_window()
