import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.maximize_window()

location = driver.find_element(By.CSS_SELECTOR,'#su')
action = ActionChains(driver)
# 鼠标双击事件
action.double_click(location).perform()

time.sleep(4)
driver.close()