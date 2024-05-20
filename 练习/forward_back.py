import time
"""
游览器前进和后退
"""
from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("https://www.baidu.com")
time.sleep(2)

driver.get("http://www.bilibili.com")
time.sleep(2)

# 游览器后退
driver.back()
time.sleep(2)

# 游览器前进
driver.forward()
time.sleep(2)

driver.close()