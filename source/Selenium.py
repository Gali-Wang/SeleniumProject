from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def setBrowser():
    option = Options()
    option.add_experimental_option("detach", True)
    #option.add_argument("--no-sandbox")

    browser = webdriver.Chrome(options=option)
    return browser


browser = setBrowser()
browser.get("https://www.baidu.com")



'''
browser.get_screenshot_as_file('../img/screenshot.png') #浏览器截图
time.sleep(3)
browser.maximize_window() #最大化
time.sleep(3)
browser.close() #关闭该标签页
time.sleep(2)
browser.refresh() #刷新页面
time.sleep(3)
browser.quit() #关闭浏览器
'''


searchItem = browser.find_element(By.ID, "kw").send_keys("原神")
browser.find_element(By.ID, "su").click()

