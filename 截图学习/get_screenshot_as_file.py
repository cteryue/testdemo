import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')

driver.find_element(By.CSS_SELECTOR,'#kw').send_keys("测试")
# 截图当前页面
time.sleep(3)
driver.get_screenshot_as_file("D://python-learn//automation_test01//File//test_01.png")

time.sleep(2)
driver.close()



