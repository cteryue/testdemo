import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.iviewui.com/view-ui-plus/component/form/cascader")

# 打开级联选择
driver.find_element(By.XPATH,'//input[@class = "ivu-input ivu-input-default"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//li[contains(text(),"江苏")]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//li[contains(text(),"苏州")]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//li[contains(text(),"拙政园")]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//i[@class = "ivu-icon ivu-icon-ios-arrow-down ivu-cascader-arrow"]').click()


time.sleep(3)
driver.close()