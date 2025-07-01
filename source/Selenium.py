from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

option = Options()
option.add_experimental_option("detach", True)
#option.add_argument("--no-sandbox")


browser = webdriver.Chrome(options=option)

browser.get("https://www.baidu.com")
time.sleep(3)
browser.maximize_window()
